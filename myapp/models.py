from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    Username = models.CharField(max_length=256, unique=True, null=True, blank=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    address = models.TextField()
    password = models.CharField(max_length=100)
    Gender = models.CharField(max_length=6)
    age = models.CharField(max_length=20)
    Profile_pic = models.FileField(upload_to = 'profile_pic' , default='pic.jpg')

    def __str__(self):
        return self.Username

class Pass(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE ,null=True, blank=True)
    Destination = models.CharField(max_length=256, null=True, blank=True)
    From = models.CharField(max_length=256,null=True, blank=True)
    To = models.CharField(max_length=256, null=True, blank=True)
    Distance = models.CharField(max_length=256, null=True, blank=True)
    Duration = models.CharField(max_length=30, null=True, blank=True)
    Issue_date = models.CharField(max_length=30,null=True, blank=True)
    End_date = models.CharField(max_length=30,null=True, blank=True)
    Pass_amount = models.CharField(max_length=10)

    def __str__(self):
        return self.User.Username