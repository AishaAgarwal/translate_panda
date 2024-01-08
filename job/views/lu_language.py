from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..models import get_language_lookup
from utils.auth import FirebaseAuthentication

class LuLanguageView(APIView):
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        """Getting list of language."""
        data = get_language_lookup()
        if len(data) == 0:
            status_code = status.HTTP_204_NO_CONTENT
        else:
            status_code = status.HTTP_200_OK
        return Response(data, status=status_code)