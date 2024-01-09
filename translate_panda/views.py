from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from utils.auth import FirebaseAuthentication
from rest_framework.renderers import TemplateHTMLRenderer
import json
import os
from django.shortcuts import redirect


class HomeView(APIView):
    # authentication_classes = [FirebaseAuthentication]
    # permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'
    
    def get(self, request):
        try:
            return Response({'serializer': 'sample data'}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(json.dumps({'Message': 'Internal Server Error'}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProtectedAreaView(APIView):
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard.html'
    
    
    def get(self, request):
        try:
            return Response({'serializer': 'sample data'}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(json.dumps({'Message': 'Internal Server Error'}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DashboardOneView(APIView):
    # authentication_classes = [FirebaseAuthentication]
    # permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard_1.html'
    
    def get(self, request):
        try:
            return Response({'serializer': 'sample data'}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(json.dumps({'Message': 'Internal Server Error'}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DashboardTwoView(APIView):
    # authentication_classes = [FirebaseAuthentication]
    # permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard_2.html'
    
    
    def get(self, request):
        try:
            return Response({'serializer': 'sample data'}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(json.dumps({'Message': 'Internal Server Error'}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class DeleteVideoView(APIView):
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard.html'
    
    
    def post(self, request):
        try: 
            msg = "Video deleted, click to return!"
            os.remove('Wav2lip/results/result_voice.mp4')
        except Exception as error:
            msg = "Error: " + error 
            return redirect("protected_area") 
        return Response({'serializer': 'sample data'}, status=status.HTTP_200_OK)

