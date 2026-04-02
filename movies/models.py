from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    release_date = models.DateField()
    video_file = models.FileField(upload_to="movies/")
    thumbnail = models.ImageField(upload_to="thumbnails/")

    def __str__(self):
        return self.title
