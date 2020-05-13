
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse 
from django.views import generic 
from django.http import HttpResponseRedirect

from .models import *
from .forms import MusicianForm, AlbumForm, SongForm


#Home view
def home(request):
    context = {
        'musicians': Musician.objects.all()
    }
    return render(request, 'music/home.html', context)




    def get(self, request, musician_id):
        form = AlbumForm()
        musician = Musician.objects.get(id=musician_id)
        context = {'form': form, "musician": musician}
        return render(request, "music/new/new_album.html", context)

    def post(self, request, musician_id):
        # TODO: save musician to data base then redirect to add album page or song page
        if request.method == "POST":
            form = AlbumForm(request.POST)
            if form.is_valid():
                
                album = form.save(commit=False)
                
                album.artist = Musician.objects.get(id=musician_id)
                album.save()

                return HttpResponseRedirect(reverse('music:album_detail', kwargs={'album_id': album.id}))

            else:


                errors = "Your album was not created"
                # messages.error(request, errors, extra_tags='alert')
        else:
            form = AlbumForm()

        context = {'form': form}

        return render(request, 'music/new/album_new.html', context)

class NewMusician(generic.CreateView):
    model = Musician

    def get(self, request):
        # user = request.user
        # olive = OliveOil.objects.get(pk=olive_id)
        form = MusicianForm()

        context = {'form': form}
        return render(request, "music/new/music_new.html", context)

    def post(self, request):
    # TODO: save musician to data base then redirect to add album page or song page
        if request.method == "POST":
            form = MusicianForm(request.POST)
            if form.is_valid():
                
                musician = form.save(commit=False)
                
                musician.save()

                print(musician)

                # return render(request, 'music/musician_detail.html', {'musician': musician})
                return HttpResponseRedirect(reverse('music:musician_detail', kwargs={'musician_id': musician.id}))

            else:


                errors = "Your musician was not created"
                # messages.error(request, errors, extra_tags='alert')
        else:
            form = MusicianForm()

        context = {'form': form}

        return render(request, 'music/new/music_new.html', context)

class MusicianDetail(generic.CreateView):

    def get(self, request, musician_id):
        albums = Album.objects.filter(artist=musician_id)
        context = { 'musician': Musician.objects.get(id=musician_id), 'albums': albums}
        return render(request, 'music/musician_detail.html', context)
    
    def post(self, request):
        pass


class NewAlbum(generic.CreateView):

    def get(self, request, musician_id):
        form = AlbumForm()

        context = {'form': form}
        return render(request, "music/new/album_new.html", context)

    def post(self,request, musician_id):
    # TODO: save musician to data base then redirect to add album page or song page
        if request.method == "POST":
            form = AlbumForm(request.POST)
            if form.is_valid():
                
                album = form.save(commit=False)
                album.artist = Musician.objects.get(id=musician_id)
                album.save()

                # return render(request, 'music/musician_detail.html', {'musician': musician})
                return HttpResponseRedirect(reverse('music:album_detail', kwargs={'album_id': album.id}))

            else:
                errors = "Your song was not created"
                # messages.error(request, errors, extra_tags='alert')
        else:
            form = AlbumForm()

        context = {'form': form}

        return render(request, 'music/new/album_new.html', context)

class AlbumDetail(generic.CreateView):

    def get(self, request, album_id):
        context = { 'album': Album.objects.get(id=album_id)}
        return render(request, 'music/album_detail.html', context)
    
    def post(self, request):
        pass


class NewSong(generic.CreateView):

    def get(self, request, musician_id, album_id):
        form = SongForm()

        context = {'form': form}
        return render(request, "music/new/song_new.html", context)

    def post(self,request, musician_id, album_id):
    # TODO: save musician to data base then redirect to add album page or song page
        if request.method == "POST":
            form = SongForm(request.POST)
            if form.is_valid():

                song = form.save(commit=False)
                song.album = Album.objects.get(id=album_id)
                song.artist = Musician.objects.get(id=musician_id)
                song.save()

                # return render(request, 'music/musician_detail.html', {'musician': musician})
                return HttpResponseRedirect(reverse('music:song_detail', kwargs={'song_id': song.id}))

            else:
                errors = "Your song was not created"
                # messages.error(request, errors, extra_tags='alert')
        else:
            form = SongForm()

        context = {'form': form}

        return render(request, 'music/new/song_new.html', context)

class SongDetail(generic.CreateView):

    def get(self, request, song_id):
        context = { 'song': Song.objects.get(id=song_id)}
        return render(request, 'music/song_detail.html', context)
    
    def post(self, request):
        pass

class ResultView(generic.CreateView):

    def get(self, request, album_id):
        context = { 'album': Album.objects.get(id=album_id)}
        return render(request, 'music/album_detail.html', context)
    
    def post(self, request):
        pass