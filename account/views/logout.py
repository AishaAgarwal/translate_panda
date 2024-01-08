from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from utils.auth import FirebaseAuthentication
class LogoutView(APIView):
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # Logout is just removing token from frentend side.
        return Response({'messgae': 'User logout.'}, status=status.HTTP_200_OK)