from rest_framework import serializers
from ..models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = [
            'created_from',
            'created_date',
            'updated_date',
        ]
        read_only_fields = ['id', 'passed']


class BookSerializer(serializers.ModelSerializer):
    author_first_name = serializers.SerializerMethodField()
    author_last_name = serializers.SerializerMethodField()

    class Meta:
        model = Book
        exclude = [
            'created_from',
            'created_date',
            'updated_date',
        ]
        read_only_fields = ['id']

    def get_author_first_name(self, obj):
        return obj.author.first_name

    def get_author_last_name(self, obj):
        return obj.author.last_name