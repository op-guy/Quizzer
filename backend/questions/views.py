from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Question
from .serializers import QuestionSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def allQuestionsView(request):
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
def questionByTopic(request):
    if request.method == 'POST':
        questions = Question.objects.filter(topic=request.data['topic'])
        question_serializer = QuestionSerializer(questions, many=True)
        return Response(question_serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def updateQuestion(request, id):
    try:
        question = Question.objects.all()[id - 1]
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        question_serializer = QuestionSerializer(question)
        return Response(question_serializer.data, status=status.HTTP_200_OK)


    elif request.method == 'PUT':
        question_serializer = QuestionSerializer(question, data=request.data)
        if question_serializer.is_valid():
            question_serializer.save()
            return Response(question_serializer.data, status=status.HTTP_200_OK)
        return Response(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)