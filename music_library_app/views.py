from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MusicSerializer
from .models import Song


# Class Based Views

class SongList(APIView):
    def get (self, request):
        songs = Song.objects.all()
        serializer = MusicSerializer(songs,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MusicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SongDetail(APIView):
    
    def get(self, request, pk):
        song = get_object_or_404(Song, pk=pk)
        serializer = MusicSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)  

    def put(self, request, pk):
        song = get_object_or_404(Song, pk=pk)
        serializer = MusicSerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True) 
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def delete(self, request, pk):
        song = get_object_or_404(Song, pk=pk)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

