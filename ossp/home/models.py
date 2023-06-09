from django.db import models
from login.models import User

class Question(models.Model):
    content = models.TextField()

class Answer(models.Model):
    content = models.TextField()

class ChatRoom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    last_date = models.DateTimeField()

class ChatSet(models.Model):
    ChatRoom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)    #소속된 ChatRoom 정보
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)    #포함한 Question
    Answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)    #포함한 Answer
    create_date = models.DateTimeField(auto_now_add=True)