from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()

#Database model that stores each list
class TList(models.Model):
    name = models.CharField(max_length=120)
    city = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    #Count likes per list, each user can like once, thus we just add a user to the list when he likes, we count likes with: list.likes.count()
    likes = models.ManyToManyField(User, related_name='liked_lists')
    is_public = models.BooleanField(default=True)
    #When Modelclass is printed, print the name instead of the model instance
    def __str__(self):
        return self.name

#Database model that stores each Location/Element from a list
class Element(models.Model):
    tlist = models.ForeignKey(TList, on_delete=models.CASCADE, related_name='elements')
    name = models.CharField(max_length=255)
    	
    def __str__(self):
    	return self.name