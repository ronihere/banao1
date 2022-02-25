from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    fname=models.CharField(max_length=30,blank=True)
    lname=models.CharField(max_length=30,blank=True)
    img=models.ImageField(blank=True)
    address=models.CharField(max_length=300,blank=True)

    def __str__(self):
        return self.user.username
