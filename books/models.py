from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

class Book(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE, default=1)
    title = models.CharField("Title", max_length=200)
    description = models.TextField("Description")
    isbn = models.CharField("Isbn", max_length=200)
    cover = models.URLField("Cover", max_length=500)
    publisher = models.CharField("Publisher", max_length=200)
    pub_date = models.DateTimeField()
    author = models.CharField("Author", max_length=100)
    customer_review_rank = models.FloatField("Customer review rank", null=True, blank=True)

    def __str__(self):
        return self.title


class Thread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='threads', default=1)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)  # 선택값 허용
    reading_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    thread = models.ForeignKey("thread", on_delete=models.CASCADE, related_name='comment', default=1)
    content = models.TextField(null=True, blank=True)  # 선택값 허용
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    def __str__(self):
        return self.title