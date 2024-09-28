from django.contrib import admin
from .models import Post

# Register your models here.
#if we want to see models that we have been created inside admin dashboard , we need to add them here

admin.site.register(Post)