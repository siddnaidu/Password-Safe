from django.contrib import admin
from .models import Profile, Account

# Register your models here.

admin.site.register(Account)
admin.site.register(Profile)