# uploader/urls.py
from django.urls import path
from .views import FileUploadView, healthcheck

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('healthcheck/', healthcheck),
]
