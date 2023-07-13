from django.shortcuts import render

# Create your views here.

def conversations(request):
    return render(request, 'conversations.html')

def chat(request):
    return render(request, 'chat.html')

def index(request):
    return render(request, 'index.html')

def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})
