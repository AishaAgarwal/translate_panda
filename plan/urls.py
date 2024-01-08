from django.urls import path

from .views import LuPlanView, UpdateView, CreateCheckOutSessionView, SuccessView, CancelView

app_name = "plan"

urlpatterns = [
    path('lu_plan/', LuPlanView.as_view(), name='lu_plan'),
    path('update/', UpdateView.as_view(), name='update'),
    path('success/', SuccessView.as_view(), name='success_view_name'),
    path('cancel/', CancelView.as_view(), name='cancel_view_name'),
    path('create-checkout-session/<str:price_id>/', CreateCheckOutSessionView.as_view(), name='create-checkout-session'),
]