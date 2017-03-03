from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    likes = models.IntegerField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title