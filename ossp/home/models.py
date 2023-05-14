from django.db import models

class ChatRoom(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    last_date = models.DateTimeField()

class Question(models.Model):
    ChatRoom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()