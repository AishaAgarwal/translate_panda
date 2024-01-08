from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from utils.auth import FirebaseAuthentication

from ..models import filter_job

class ListView(APIView):
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Getting user
        username = request.user.username
        
        # Getting job list
        jobs = filter_job(username)
        return Response(jobs, status=status.HTTP_200_OK)