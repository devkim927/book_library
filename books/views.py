import os
import re
from django.conf import settings
from .models import Book, Thread, Category, Comment
from .serializers import BookListSerializer, CategoryListSerializer, CommentListSerializer, ThreadListSerializer
from gtts import gTTS
import requests  # AI API 호출을 위한 requests 모듈
import openai
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def index(request):
    books = Book.objects.all()
    serializer = BookListSerializer(books, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def category(request):
    categories = Category.objects.all()
    serializer = CategoryListSerializer(categories, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET'])
def detail(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookListSerializer(book)
    return Response(serializer.data)

@api_view(['GET'])
def thread(request, thread_pk, book_pk):
    book = Book.objects.get(pk=book_pk)
    thread = Thread.objects.get(pk=thread_pk)
    serializer = ThreadListSerializer(thread)
    return Response(serializer.data)



@api_view(['POST'])
def create_thread(request):
    serializer = CommentListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)        
    return Response(serializer.errors, status=status.HTTP_400_REQUEST)

@api_view(['POST'])
def create_comment(request):
    serializer = CommentListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)        


@api_view(['GET', 'PUT', 'POST'])
def comment_detail(request,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentListSerializer(comment)
        return Response(serializer.data)        

    elif request.method == 'PUT':
        serializer = CommentListSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'POST':
        serializer = CommentListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
