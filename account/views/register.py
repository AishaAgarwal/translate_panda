from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings

from ..serializers import RegisterSerializer
from plan.models import update_plan

class RegisterView(APIView):
    def _validate(self, data):
        email = data.get('email')
        if email is None:
            return 'ERROR: email is not provided.', status.HTTP_400_BAD_REQUEST
        
        password = data.get('password')
        if password is None:
            return 'ERROR: password is not provided.', status.HTTP_400_BAD_REQUEST
        
        password2 = data.get('password2')
        if password2 is None:
            return 'ERROR: password2 is not provided.', status.HTTP_400_BAD_REQUEST
        
        if password != password2:
            return 'ERROR: Password mismatch.', status.HTTP_400_BAD_REQUEST
        return data, status.HTTP_200_OK
    
    def post(self, request):
        # Getting data
        data = request.data
        rd, sc = self._validate(data)
        if sc != 200:
            return Response(rd, sc)
        
        # Making user in firebase
        try:
            email = data.get('email')
            password = data.get('password')
            login = settings.AUTH.create_user_with_email_and_password(email, password)
        except:
            return Response('ERROR: Given email already exists.', status=status.HTTP_400_BAD_REQUEST)
        
        try:
            data = data.dict()
        except:
            pass
        data['username'] = login['localId']
        serializer = RegisterSerializer(data=data)
        # Saving data
        if serializer.is_valid():
            serializer.save()
            
        # Adding free plan
        update_plan(login['localId'], 'free')
        return Response('User creates successfully.', status=status.HTTP_201_CREATED)