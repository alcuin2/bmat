from django.urls import path
from .views import FileViewSet

file_list = FileViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

file_detail = FileViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

file_works = FileViewSet.as_view({
    'get': 'works'
})

file_work = FileViewSet.as_view({
    'get': 'work'
})

urlpatterns = [
   path('files', file_list, name='file-list'),
   path('files/<int:pk>', file_detail, name='file-detail'),
   path('files/<int:pk>/works', file_works, name='file-works'),
   path('files/<int:pk>/works/<int:work_id>', file_work, name='file-work'),
]
