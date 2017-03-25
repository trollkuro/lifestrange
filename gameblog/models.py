from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    likes = models.IntegerField(default=0)

    def approve(self):
        self.save()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Photo(models.Model):
    name = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey('gameblog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, related_name='replies')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text