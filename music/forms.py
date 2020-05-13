from django import forms
from music.models import Musician, Album, Song


class MusicianForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:

        model = Musician
        fields = '__all__'
        # exclude = ["author", "olive_id"]
        # widgets = {
        #     'full_name': forms.TextInput(attrs={'placeholder': 'John Doe'}),
        #     'email': forms.TextInput(attrs={'placeholder': 'Enter your email'}),
        #     'phone_number': forms.TextInput(attrs={'placeholder': '###-###-####'}),
        # }

class AlbumForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = Album
        fields = '__all__'
        exclude = ["artist"]


class SongForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = Song
        fields = '__all__'
        exclude = ["artist", "album"]

# class MusicianForm(forms.ModelForm):
#     """ Render and process a form based on the Page model. """
#     class Meta:
#         model = Musician
#         fields = '__all__'