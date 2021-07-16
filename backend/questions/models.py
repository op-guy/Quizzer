from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=200)
    topic = models.CharField(max_length=50)
    answers = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=100)