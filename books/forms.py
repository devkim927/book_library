from django import forms
from .models import Book,Thread

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # 'image'와 'content' 대신 'cover_image'와 'description'을 사용합니다.
        fields = ['title', 'description', 'customer_review_rank', 'author', 'cover_image']

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title','content','read_date','cover_image']

        