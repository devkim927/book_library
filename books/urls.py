# books/urls.py

from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("books/", views.index, name="index"),
    path("category/", views.category, name="category"),
    path("<int:pk>/", views.detail, name="detail"),
    path("create/", views.create, name="create"),
    path('threads/',views.thread),
    path('threads/<int:thread_pk>/', views.thread_detail, name='thread_detail'),
    path('<int:book_pk>/threads/create/', views.thread_create, name='thread_create'),
    path('<int:thread_pk>/comments/create/', views.comment_create, name='comment_create'),
    path('<int:thread_pk>/comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
]
