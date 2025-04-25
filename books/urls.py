# books/urls.py

from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.index, name="index"),
    path("category/", views.category, name="category"),
    path("<int:pk>/", views.detail, name="detail"),
    path("create/", views.create, name="create"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path('<int:book_pk>/threads/create/', views.thread_create, name='thread_create'),
    path('<int:book_pk>/threads/<int:thread_pk>/', views.thread_detail, name='thread_detail'),
    path('<int:book_pk>/threads/<int:thread_pk>/update/', views.thread_update, name='thread_update'),
    path('<int:book_pk>/threads/<int:thread_pk>/delete/', views.thread_delete, name='thread_delete'),
    path('<int:book_pk>/threads/<int:thread_pk>/like/', views.like, name='like'),
    path('<int:thread_pk>/comments/create/', views.comment_create, name='comment_create'),
    path('<int:thread_pk>/comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
    path('<int:thread_pk>/comments/<int:comment_pk>/update/', views.comment_update, name='comment_update'),
    path('<int:thread_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),    
]
