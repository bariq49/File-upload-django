from rest_framework import serializers
from .models import *
import shutil

class FilesList_Serializer(serializers.Serializer):
    files = serializers.ListField(
        child = serializers.FileField(max_length = 10000,  allow_empty_file = False, use_url = False)
    )
    folder = serializers.CharField(required = False)

    def zip_files(self, folder):
        shutil.make_archive(f'static/zip/{folder}', "zip", f"media/{folder}")


    def create(self, validated_data):
        folder = Folder.objects.create()
        files_objs = []
        files = validated_data.pop('files')
        for file in files:
            file_obj = Files.objects.create(folder = folder, file = file)
            files_objs.append(file_obj)
        
        self.zip_files(folder.uid)

        return {'files' : {}, 'folder': str(folder.uid)}