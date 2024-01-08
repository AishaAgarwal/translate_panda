from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from utils.auth import FirebaseAuthentication
from django.shortcuts import redirect

from ..models import get_plan_lookup
from rest_framework.renderers import TemplateHTMLRenderer
import json, stripe
from django.urls import reverse


class LuPlanView(APIView):
    # authentication_classes = [FirebaseAuthentication]
    # permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'plans.html'
    
    def get(self, request):
        """Getting list of plans."""
        data = get_plan_lookup()
        if len(data) == 0:
            status_code = status.HTTP_204_NO_CONTENT
        else:
            status_code = status.HTTP_200_OK
        print(data)
        return Response({'data': data}, status=status.HTTP_200_OK)


class CreateCheckOutSessionView(APIView):
    def post(self, request, price_id, *args, **kwargs):
        try:
            price_with_id = 'price_' + price_id
            success_url = reverse('plan:success_view_name')
            cancel_url = reverse('plan:cancel_view_name')

            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        # 'price': 'price_1OHKWmESjDp0Y3E0x29CrBUi',
                        'price': price_with_id,
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=success_url,
                cancel_url=cancel_url,
            )
        except Exception as e:
            error = 'Internal Server Error' + e
            return Response(json.dumps({'Message': error}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

        return redirect(checkout_session.url, code=303)


class SuccessView(APIView):
    # authentication_classes = [FirebaseAuthentication]
    # permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'success.html'
    
    def get(self, request):
        try:
            return Response({'serializer': 'sample data'}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(json.dumps({'Message': 'Internal Server Error'}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CancelView(APIView):
    # authentication_classes = [FirebaseAuthentication]
    # permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cancel.html'
    
    def get(self, request):
        try:
            return Response({'serializer': 'sample data'}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(json.dumps({'Message': 'Internal Server Error'}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
