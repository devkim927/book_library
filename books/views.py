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
