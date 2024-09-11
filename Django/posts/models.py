from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    content = models.TextField()
    slug = models.SlugField()
    date_time = models.DateTimeField(auto_now_add=True)
