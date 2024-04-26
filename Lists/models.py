#Lists/models.py

from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()

class TList(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=30, blank=True, null=True)  # Optional location field
    author = models.ForeignKey(User, related_name='tlists', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_lists', blank=True)  # Store users who liked the list
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name

#Database model that stores each Location/Element from a list
class Element(models.Model):
    tlist = models.ForeignKey(TList, on_delete=models.CASCADE, related_name='elements')
    name = models.CharField(max_length=255)
    	
    def __str__(self):
    	return self.name