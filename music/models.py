from django.db import models


class Musician(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50)
    publish_date = models.DateField(null=True)

    def __str__(self):
        return self.name 


class Song(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    num_stars = models.IntegerField(default=0)

    def __str__(self):
        return self.name 