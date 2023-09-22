from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FileInputSerializer, FileOutputSerializer
from .services import file_create, file_process, get_file_extension, file_list


class FileCreateApi(APIView):

    def post(self, request):
        serializer = FileInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file = file_create(**serializer.validated_data)
        file_extension = get_file_extension(request.FILES['file'])
        file_process(file.id, file_extension)
        return Response(data={'id': file.id, 'uploaded_at': file.uploaded_at, 'processed': file.processed},
                        status=status.HTTP_201_CREATED)


class FileListApi(APIView):

    def get(self, request):
        files = file_list()

        data = FileOutputSerializer(files, many=True).data

        return Response(data)

