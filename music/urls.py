from django.contrib import admin
from django.urls import include, path
from . import views

# urlpatterns = [
#     path('', views.home, name="home"),
#     path('musician/<int:musician_id>', views.artist, name="artist"),
#     path('album/<int:album_id>', views.album, name="album"),
#     path('song/<int:song_id>', views.song, name="song")
# ]

app_name = 'music'

urlpatterns = [

    path('', views.home, name='home'),
    
    path('album/new/<int:musician_id>', views.NewAlbum.as_view(), name='new_album'),
    path('music/album_detail/<int:album_id>/', views.AlbumDetail.as_view(), name='album_detail'),
    
    path('music/new', views.NewMusician.as_view(), name='new_musician'),
    path('musician/<int:musician_id>/', views.MusicianDetail.as_view(), name='musician_detail'),

    path('music/song/<int:song_id>', views.SongDetail.as_view(), name='song_detail'),
    path('song/new/<int:musician_id>/<int:album_id>', views.NewSong.as_view(), name='new_song'),

    path('musician/results/<int:musician_id>', views.ResultView.as_view(), name='results_view'),

    ]



