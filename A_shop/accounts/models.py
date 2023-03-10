from django.db import models
from django.contrib.auth.models import User


class Profiles(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    open = models.BooleanField(default=True)


