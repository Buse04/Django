from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# When you add new models here, you need to type makemigration commnet on terminal

class Post(models.Model):
    title = models.CharField(max_length=75)
    content = models.TextField()
    slug = models.SlugField()
    date_time = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.title