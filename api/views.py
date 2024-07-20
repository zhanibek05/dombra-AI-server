from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import FileSerializer
from .midi2tabs import midi2tabs
from .models import File
from .s3 import upload_file
from django.core.files.storage import default_storage

import tempfile

import os

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_instance = file_serializer.save()
            file_name = file_instance.file.name
            
            file_url = file_instance.file.url
            
            
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                tmp_file_path = tmp_file.name

                # Open the file from storage and write to the temporary file
                file_obj = default_storage.open(file_instance.file.name)
                tmp_file.write(file_obj.read())
                file_obj.close()

            try:
                # Pass the temporary file path to your midi2tabs function
                dombyra_tabs = midi2tabs(tmp_file_path)
                print(dombyra_tabs)
                return JsonResponse({"midi_data": dombyra_tabs}, safe=False, status=200)
            finally:
                # Delete the temporary file
                os.remove(tmp_file_path)
            
        else:
            return Response(file_serializer.errors, status=400)
