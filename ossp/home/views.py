from django.shortcuts import render
from .models import *

def home(request):
    chatList = ChatRoom.objects.order_by('-last_date')
    context = {'chatList':chatList}
    return render(request, 'home/homepage.html',context)