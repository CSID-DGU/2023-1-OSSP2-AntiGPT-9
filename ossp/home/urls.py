from django.urls import path, re_path
from . import views

app_name = 'homepage'
urlpatterns = [
    path('homepage/', views.home, name='homepage'),
    path('homepage/<int:chatroom_id>/', views.chat, name='chatpage'),
    path('homepage/question_send/<int:chatroom_id>/', views.question_send, name='question_send')
]
