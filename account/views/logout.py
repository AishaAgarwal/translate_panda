from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.renderers import TemplateHTMLRenderer

from utils.auth import FirebaseAuthentication
class LogoutView(APIView):
    # authentication_classes = [FirebaseAuthentication]
    # permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard.html'
    def post(self, request):
        # Logout is just removing token from frentend side.
        return Response({'messgae': 'User logout.'}, status=status.HTTP_200_OK)
        #  return redirect(reverse('account:login'))