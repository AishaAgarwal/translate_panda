from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import os
from django.conf import settings

from utils.read_write_file import write_file
from ..models import add_job, get_language_lookup
from utils import get_uuid, get_datetime
from account.models import get_user_plan
from plan.models import get_plan_detail
from utils import send_message_on_ai_queue
from utils.auth import FirebaseAuthentication

from rest_framework.renderers import TemplateHTMLRenderer

class UploadView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [FirebaseAuthentication]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard.html'
    
    def _validate(self, data):
        """Performing initial validation."""
        # File must exists
        video_file = data.getlist('video_file')
        if video_file is None:
            return 'ERROR: Video file is not provided.', status.HTTP_400_BAD_REQUEST
        
        # Single file processing is supported
        if len(video_file) != 1:
            return 'ERROR: Single video file upload is supported.', status.HTTP_400_BAD_REQUEST
        
        # Provided target language must be in registered language.
        language = data.get('target_language')
        if language is None:
            return 'ERROR: Target language is not provided.', status.HTTP_400_BAD_REQUEST
        
        target_naguage = get_language_lookup()
        if language not in target_naguage:
            return f'ERROR: Target language is not in register languages. {target_naguage}', status.HTTP_400_BAD_REQUEST
        return data, status.HTTP_200_OK
    
    def post(self, request):
        # Performing validation
        data = request.data
        rd, sc = self._validate(data)
        if sc != 200:
            return Response(rd, sc)
        
        # Generating job id
        job_id = get_uuid()
        
        # Saving file
        username = request.user.username
        video_file = data.getlist('video_file')
        for file in video_file:
            # Getting file name
            file_name = file.name
            file_dir = os.path.join(settings.MEDIA_ROOT, job_id)
            os.makedirs(file_dir, exist_ok=True)
            file_path = os.path.join(file_dir, file_name)
            
            # Writing file to location.
            file_data = file.read()
            write_file(file_path, file_data)
            
        # Checking host and port
        host, port = os.environ.get('HOST'), os.environ.get('PORT')
        if (host and port):
            file_url = f'http://{host}:{port}/{file_path}'
        else:
            file_url = None
            
        # Getting target language
        target_language = data.get('target_language')
        
        # Getting priority
        user_plan = get_user_plan(username)
        plan_detail = get_plan_detail(user_plan)
        plan_priority = plan_detail['priority']
        
        # Making job data
        data = {
            'created_by': username,
            'created_at': get_datetime(),
            'status': 'send_to_ai',
            'progress': 0,
            'file_path': file_path,
            'file_url': file_url,
            'file_name': file_name,
            'file_directory': file_dir,
            'target_language': target_language
        }
        
        # Send data to AI for processing.
        send_data = {'metadata': {'request_id': job_id}, 'data': data}
        try:
            is_sent = send_message_on_ai_queue(send_data, plan_priority)
        except:
            is_sent = False
        if is_sent:
            data['status'] = 'send_to_ai'
        else:
            data['status'] = 'backend_ai_com_error'
        
        # Adding job data
        add_job(job_id, data)
        return Response({'message': 'Upload successful.'}, status=status.HTTP_200_OK)