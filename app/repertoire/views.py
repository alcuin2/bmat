from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import File, Work
from .serializer import FileSerializer, WorkSerializer

class FileViewSet(viewsets.ModelViewSet):

    queryset = File.objects.all()
    serializer_class = FileSerializer

    @action(detail=True)
    def works(self, request, *args, **kwargs):
        file = self.get_object()
        works = file.works.all()
        count = len(works)
        work_serializer = WorkSerializer(works, many=True)
        file_serializer = FileSerializer(file) 
        return Response({
            'count': count,
            'works': work_serializer.data,
            'file': file_serializer.data
        })

    @action(detail=True)
    def work(self, request, *args, **kwargs):
        file = self.get_object()
        work_id = self.kwargs.get('work_id', None)
        work = Work.objects.filter(pk=work_id, file=file).first()
        if(work is None):
            return Response({
                "detail": "Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
        work_serializer = WorkSerializer(work)
        return Response(work_serializer.data)




