from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import customUser
# Register your models here.
admin.site.register(customUser, UserAdmin)
