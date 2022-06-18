from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()
# Create your models here.


class Post (models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    Author = user.get_username
    Created_data = models.DateTimeField()
    Published_data = models.DateTimeField()

    # def __str__(self) -> str:
    #     return self.name
