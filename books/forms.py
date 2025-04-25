from django import forms
from .models import Book, Thread, Category, Comment

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # 'image'와 'content' 대신 'cover_image'와 'description'을 사용합니다.
        fields = ['title', 'description', 'isbn', 'cover', 'publisher', 'pub_date', 'author', 'customer_review_rank']

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title','content','reading_date']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        exclude = ['created_at', 'updated_at'] 
