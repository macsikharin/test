from rest_framework import serializers
from .models import Book, Category, Author


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    author = AuthorSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ['code', 'name', 'description', 'category', 'author', 'price']
