from django.shortcuts import render, redirect, Http404
from django.urls import reverse
from django.utils import timezone
from login.models import User
from .models import *
import requests
import json
import openai
from django.http import HttpResponse


def test(request):
    return render(request, 'home/chat.html')

def room_delete(request, user_id, del_id):
    if request.method == 'POST':
        target = ChatRoom.objects.filter(user__id=user_id, id=del_id)
        
        if target:
            target.delete()
            url = reverse('homepage:homepage',args=[user_id])
            return redirect(url)
        else:
            raise Http404("No such object")
#=================================================================================

#로그인 후 사용자에게 할당된 첫 페이지(새 채팅)
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
        standard_ques = request_aimodel(input_text)
        translated_answer = request_chatgpt(standard_ques)
        answer = Answer.objects.create(content=translated_answer)
        ChatSet.objects.create(ChatRoom=room,Question=ques, Answer=answer)    #새로운 방에 역참조되는 문답 객체 생성
        url = reverse('homepage:chatpage',args=(user_id, room.id))
        return redirect(url)

#=================================================================================

#존재하는 채팅방에 대한 페이지
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
        standard_ques = request_aimodel(input_text)
        translated_answer = request_chatgpt(standard_ques)
        answer = Answer.objects.create(content=translated_answer)
        ChatSet.objects.create(ChatRoom=room,Question=ques, Answer=answer) 
        url = reverse('homepage:chatpage',args=(user_id, room.id))
        return redirect(url)

#=================================================================================

# api 통신, dialect String 입력, standard String 반환
def request_aimodel(dialect):
    # dialect seriallization
    dialect_dict = {"dialect":f"{dialect}"}
    request_dialect = json.dumps(dialect_dict)

    # standard transfer, jeju model api request
    standard = requests.post("http://4.194.73.164:8010/jeju", data=request_dialect)
    standard = standard.json()["standard"]

    return standard


def request_chatgpt(message):
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'system', 'content': 'You are a user'}, {'role': 'user', 'content': message}
        ]
    )

    # ChatGPT 답변 반환
    chatgpt_response = response["choices"][0]["message"]["content"]
    if chatgpt_response:
        return chatgpt_response