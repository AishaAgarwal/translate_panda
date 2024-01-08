"""
URL configuration for translate_panda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import HomeView, DashboardOneView, DashboardTwoView, ProtectedAreaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='index'),
    path('protected_area/', ProtectedAreaView.as_view(), name='protected_area'),
    path('dashboard_1/', DashboardOneView.as_view(), name='dashboard_1'),
    path('dashboard_2/', DashboardTwoView.as_view(), name='dashboard_2'),
    path('account/', include('account.urls')),
    path('job/', include('job.urls')),
    path('plan/', include('plan.urls')),
]
