from django.shortcuts import render, redirect, Http404
from django.urls import reverse
from django.utils import timezone
from urllib.parse import quote, unquote
from django.core import signing
from login.models import User
from .models import *
import requests
import json


def test(request):
    return render(request, 'home/chat.html')

def parseUrl(input_url):
    count = 0
    type = ""

    components = input_url.strip('/').split('/')
    count = len(components)

    if components[1].isdigit():
        if count == 2: type = 'home'
        elif 'question_send' in components:
            if count == 3: type = 'question_send_initial'
            else: type = 'question_send'
        else:
            if count ==3: type = 'chat'
            else: type = 'room_delete'
    else:
        type = components[1]

    return type, components

def get_encrypted_url(param):
    signed_value = signing.dumps(param)
    return f"?p={signed_value}"
    
#=================================================================================

def room_delete(request, user_id, del_id):
    if request.method == 'POST':
        target = ChatRoom.objects.get(user__id=user_id, id=del_id)
        target_sets = ChatSet.objects.filter(ChatRoom=target)

        if target:
            #모든 문답 지움
            for set in target_sets:
                if set.Answer:
                    set.Answer.delete()
                if set.Question:
                    set.Question.delete()
            #모든 세트 지움
            target_sets.delete()
            #채팅방 지움
            target.delete()
            url = reverse('homepage:homepage',args=[user_id])
            return redirect(reverse('homepage:process') + get_encrypted_url(url))
        else:
            raise Http404("No such object")
#=================================================================================

#로그인 후 사용자에게 할당된 첫 페이지(새 채팅)
def home_v(request, user_id):
    url = reverse('homepage:homepage',args=[user_id])
    return redirect(reverse('homepage:process') + get_encrypted_url(url))

def home(request, user_id):
    user_chatList = ChatRoom.objects.filter(user__id = user_id).order_by('-last_date')
    context = {'chatList':user_chatList, 'user_id':user_id}
    return render(request, 'home/homepage.html', context)
#첫 질문
def question_send_initial(request, user_id):
    if request.method == 'POST':
        input_text = request.POST['input_text'] #요청된 질문 문자열
        ques = Question.objects.create(content=input_text)  #질문 객체 생성
        subj = input_text   #질문 내용 그대로 제목 설정하고,
        if len(subj) > 10:  #질문 내용 길이 10 초과부터 잘라내서 제목으로 사용
            subj = subj[:10] + "..."
        usr = User.objects.get(id = user_id)    #요청된 user_id에 해당하는 유저 객체 찾기
        room = ChatRoom.objects.create(user=usr, subject=subj, last_date=timezone.now())    #앞선 유저, 제목 객체들을 인자로 모아서 현시간부로 새로운 방 생성
        ChatSet.objects.create(ChatRoom=room, Question=ques) #새로운 방에 역참조되는 문답 객체 생성
        url = reverse('homepage:chatpage',args=(user_id, room.id))
        return redirect(reverse('homepage:process') + get_encrypted_url(url))

#=================================================================================

#존재하는 채팅방에 대한 페이지
def chat_v(request, user_id, chatroom_id):
    url = reverse('homepage:chatpage',args=(user_id, chatroom_id))
    return redirect(reverse('homepage:process') + get_encrypted_url(url))

def chat(request, user_id, chatroom_id):
    user_chatList = ChatRoom.objects.filter(user__id = user_id).order_by('-last_date')
    sets = ChatRoom.objects.get(user__id = user_id, id=chatroom_id).chatset_set.all()
    context = {'chatList':user_chatList, 'user_id':user_id, 'sets':sets, 'chat_id':chatroom_id}
    return render(request, 'home/chatpage.html', context)
#존재하는 채팅방에 대한 추가 질문
def question_send(request, user_id, chatroom_id):
    if request.method == 'POST':
        input_text = request.POST['input_text']
        ques = Question.objects.create(content=input_text)
        room = ChatRoom.objects.get(user__id = user_id, id=chatroom_id)
        room.last_date=timezone.now()
        ChatSet.objects.create(ChatRoom=room,Question=ques)
        url = reverse('homepage:chatpage',args=(user_id, room.id))
        return redirect(reverse('homepage:process') + get_encrypted_url(url))

#=================================================================================

def process_url(request):
    encrypted_value = request.GET.get('p')
    param = signing.loads(encrypted_value)
    (p_type, p_list) = parseUrl(param)

    if p_type == 'home':
        return home(request, p_list[1])
    elif p_type == 'question_send_initial':
        return question_send_initial(request, p_list[1])
    elif p_type == 'chat':
        return chat(request, p_list[1], p_list[2])
    elif p_type == 'question_send':
        return question_send(request, p_list[1], p_list[2])
    elif p_type == 'room_delete':
        return room_delete(request, p_list[1], p_list[3])

    raise Http404("No such Page")

#=================================================================================


# api 통신, dialect String 입력, standard String 반환
def api_commute(dialect):
    # dialect serialization
    dialect_dict = {"dialect":f"{dialect}"}
    request_dialect = json.dumps(dialect_dict)

    # standard transfer, jeju model api request
    response = requests.post("http://4.194.73.164:8010/jeju", data=request_dialect)

    return response.json()["standard"]

