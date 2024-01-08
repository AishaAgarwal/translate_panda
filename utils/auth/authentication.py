from rest_framework.authentication import BaseAuthentication
from . import exceptions
from django.contrib.auth.models import User
import firebase_admin
from firebase_admin import credentials, auth
import os


"""SETUP FIREBASE CREDENTIALS"""
cred = credentials.Certificate({
        "type" : os.environ.get('FIREBASE_ACCOUNT_TYPE'),
        "project_id" : os.environ.get('FIREBASE_PROJECT_ID'),
        "private_key_id" : os.environ.get('FIREBASE_PRIVATE_KEY_ID'),
        "private_key" : os.environ.get('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
        "client_email" : os.environ.get('FIREBASE_CLIENT_EMAIL'),
        "client_id" : os.environ.get('FIREBASE_CLIENT_ID'),
        "auth_uri" : os.environ.get('FIREBASE_AUTH_URI'),
        "token_uri" : os.environ.get('FIREBASE_TOKEN_URI'),
        "auth_provider_x509_cert_url" : os.environ.get('FIREBASE_AUTH_PROVIDER_X509_CERT_URL'),
        "client_x509_cert_url" : os.environ.get('FIREBASE_CLIENT_X509_CERT_URL')
})


default_app = firebase_admin.initialize_app(cred)


"""FIREBASE AUTHENTICATION"""
class FirebaseAuthentication(BaseAuthentication):
    """override authenticate method and write our custom firebase authentication."""
    def authenticate(self, request):
        """Get the authorization Token, It raise exception when no authorization Token is given"""
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            raise exceptions.NoAuthToken("No auth token provided")
        
        """Decoding the Token It rasie exception when decode failed."""
        id_token = auth_header.split(" ").pop()
        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise exceptions.InvalidAuthToken("Invalid auth token")
        
        """Return Nothing"""
        if not id_token or not decoded_token:
            return None
        
        """Get the uid of an user"""
        try:
            uid = decoded_token.get("uid")
            email = decoded_token.get("email")
        except Exception:
            raise exceptions.FirebaseError()
        
        
        """Get or create the user"""
        user, created = User.objects.get_or_create(username=uid, email=email)
        
        
        return (user, None)