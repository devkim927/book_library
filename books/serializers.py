from rest_framework import serializers
from .models import Book,Category,Comment,Thread

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ThreadListSerializer(serializers.ModelSerializer):
    class BookTitleeSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = ('title',)
  
    book = BookTitleeSerializer(read_only=True)
    
    class Meta:
        model = Thread
        fields = '__all__'
