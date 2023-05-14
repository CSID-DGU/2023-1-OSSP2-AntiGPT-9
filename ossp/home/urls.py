from django.urls import path, re_path
from . import views

app_name = 'homepage'
urlpatterns = [
    path('homepage/', views.home, name='homepage'),
    path('homepage/<int:chatRoom_id>', views.home, name='chatroom')
]
