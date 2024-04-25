from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    hospital = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
