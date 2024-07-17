from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import FileSerializer

from .midi2tabs import midi2tabs
from .models import File

import os


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_instance, created = File.objects.get_or_create(pk=1)

            file_instance.file = request.data['file']
            file_instance.save()
            file_path = file_instance.file.path

            dombyra_tabs = midi2tabs(file_path)
            print(dombyra_tabs)
            return JsonResponse({"midi_data": dombyra_tabs}, safe=False, status=200)
        else:
            return Response(file_serializer.errors, status=400)
