from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies')

    class Meta:
        ordering = ['-id']

class Comment(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['-id']

class Vote(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    start = models.IntegerField(default=5, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='votes')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')

    class Meta:
        ordering = ['-id']