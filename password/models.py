from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    master_password = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.username

class Account(models.Model):
    profile = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=30, null=True)
    username = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=30, null=True)
    website = models.CharField(max_length=30, null=True)

    def __str__(self) -> str:
        return self.account_name