from django.shortcuts import render
from .models import Song

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'player/song_list.html', {'songs': songs})

def song_upload(request):
    