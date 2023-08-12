from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

def home(request):
    return render(request, 'index.html')
def download(request, uid):
    pass

class HandleFilesUpload(APIView):
  
    def post(self, request):
        try:
            data = request.data
            serializer = FilesList_Serializer(data = data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': "Files uploaded successfully",
                    'data': serializer.data
                })
            
            return Response({
                    'status': False,
                    'message': serializer.errors,
                    'data':serializer.data
                })
        except Exception as e:
            print(e)
        return Response({
                    'status': False,
                    'message': "Something went wrong!",
                    'data':{}
                })
