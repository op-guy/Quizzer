from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Question
from .serializers import QuestionSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def all_questions_view(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        questions_serializer = QuestionSerializer(questions, many=True)
        return Response(questions_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        question_serializer = QuestionSerializer(data=request.data)
        if question_serializer.is_valid():
            question_serializer.save()
            return Response(question_serializer.data, status=status.HTTP_201_CREATED)
        return Response(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def question_list(request):
    if request.method == 'POST':
        questions = Question.objects.filter(topic=request.data['topic'])
        question_serializer = QuestionSerializer(questions, many=True)
        return Response(question_serializer.data, status=status.HTTP_200_OK)