from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings
from django.contrib.auth.models import User

class LoginView(APIView):
    def _validate(self, data):
        """Validating data."""
        email = data.get('email')
        if email is None:
            return 'ERROR: email is not provided.', status.HTTP_400_BAD_REQUEST
        
        password = data.get('password')
        if password is None:
            return 'ERROR: password is not provided.', status.HTTP_400_BAD_REQUEST
        return data, status.HTTP_200_OK
    
    def post(self, request, *args, **kwargs):
        data = request.data
        rd, sc = self._validate(data)
        if sc != 200:
            return Response(rd, sc)
        
        # Checking existence firebase
        email = data.get('email')
        password = data.get('password')
        try:
            login = settings.AUTH.sign_in_with_email_and_password(email, password)
        except:
            return Response('ERROR: Given email or password is incorrect.', status=status.HTTP_401_UNAUTHORIZED)
        data = {'token': login['idToken']}
        
        # Checking local database
        user = User.objects.filter(email=email)
        if not user.exists():
            user = User.objects.create(
                username=login['localId'],
                email=email
            )
            user.set_password(password)
            user.save()
        return Response(data, status=status.HTTP_200_OK)