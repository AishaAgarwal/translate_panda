from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from utils.auth import FirebaseAuthentication

from ..models import get_plan_lookup, update_plan


class UpdateView(APIView):
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated]
    
    def _validate(self, data):
        """Performing initial validation."""
        # Checking plan key
        plan = data.get('plan')
        if plan is None:
            return 'ERROR: Plan is required.', status.HTTP_400_BAD_REQUEST
        
        # Checking plan existance
        plans = get_plan_lookup()
        if plan not in plans:
            return f'ERROR: Plan `{plan}` is not provided by us.', status.HTTP_400_BAD_REQUEST
        return data, status.HTTP_200_OK
    
    def post(self, request):
        # Performing validation
        data = request.data
        rd, sc = self._validate(data)
        if sc != 200:
            return Response(rd, sc)
        
        # Updating plan
        update_plan(request.user.username, data.get('plan'))
        return Response({'message': 'Update successfull.'}, status=status.HTTP_200_OK)