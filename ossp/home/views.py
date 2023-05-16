from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *

def home(request):
    chatList = ChatRoom.objects.order_by('last_date')
    context = {'chatList':chatList}
    return render(request, 'home/homepage.html', context)

def chat(request, chatroom_id):
    chatList = ChatRoom.objects.order_by('last_date')
    sets = ChatRoom.objects.get(id = chatroom_id).chatset_set.all()
    context = {'chatList':chatList, 'sets':sets, 'chat_id':chatroom_id}
    return render(request, 'home/chatpage.html', context)

def question_send(request, chatroom_id):
    room = get_object_or_404(ChatRoom, pk=chatroom_id)
    room.chatset_set.question.create()
    room.chatset_set.create()
    return redirect('home/chatpage.html')
