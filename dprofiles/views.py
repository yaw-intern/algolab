from django.shortcuts import render
from django.http import HttpResponse
from users.models import customUser
# Create your views here.

def profiles(request, username):
    if customUser.objects.filter(username=username).exists():
        queriedUser = customUser.objects.get(username=username)
        return render(request, 'profiles.html', {'queriedUser':queriedUser})
    else:
        return HttpResponse('<h3>No such user</h3>')
    return render(request, 'profiles.html')