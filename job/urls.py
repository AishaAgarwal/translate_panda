from django.urls import path

from .views import UploadView, ListView, LuLanguageView

app_name = 'job'


urlpatterns = [
    path('upload/', UploadView.as_view(), name='upload'),
    path('list/', ListView.as_view(), name='list'),
    path('lu_target_language/', LuLanguageView.as_view(), name='lu_target_language'),    
]