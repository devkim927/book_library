from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    isbn = models.CharField(max_length=200)
    cover = models.URLField(max_length=500)
    publisher = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    author = models.CharField(max_length=100)
    customer_review_rank = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title


class Thread(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='threads')
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)  # 선택값 허용
    reading_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    

class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='comment')
    content = models.TextField(null=True, blank=True)  # 선택값 허용
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
