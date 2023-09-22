from django.urls import path, include
from .uploader import views


uploader_patterns = [
        path('upload/', views.FileCreateApi.as_view(), name='create'),
        path('files/', views.FileListApi.as_view(), name='list'),
]

urlpatterns = [
    path('uploader/', include((uploader_patterns, 'uploader'))),
]
