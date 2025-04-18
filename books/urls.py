# books/urls.py

from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.detail, name="detail"),
    path("create/", views.create, name="create"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path('<int:book_pk>/threads/create/', views.thread_create, name='thread_create'),
    path('<int:book_pk>/threads/<int:thread_pk>/', views.thread_detail, name='thread_detail'),
    path('<int:book_pk>/threads/<int:thread_pk>/update/', views.thread_update, name='thread_update'),
    path('<int:book_pk>/threads/<int:thread_pk>/delete/', views.thread_delete, name='thread_delete'),
    path('<int:book_pk>/threads/<int:thread_pk>/like/', views.like, name='like'),
]
