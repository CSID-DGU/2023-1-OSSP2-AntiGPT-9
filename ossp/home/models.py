from django.db import models

class ChatRoom(models.Model):
    subject = models.CharField(max_length=100)
    ChatSet = models.ForeignKey(ChatSet, on_delete=models.CASCADE)
    last_date = models.DateTimeField()

class ChatSet(models.Model):
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

class Question(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField()

class Answer(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField()