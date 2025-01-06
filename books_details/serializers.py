from rest_framework import serializers
from .models import BookAuthors,BookBookshelves,BookLanguages,BookSubjects, Format
from books_master.serializers import AuthorSerializer, LanguageSerializer, SubjectSerializer, BookshelfSerializer


class BookAuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthors
        fields = '__all__'

class BookBookshelvesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookBookshelves
        fields = '__all__'

class BookLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLanguages
        fields = '__all__'

class BookSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSubjects
        fields = '__all__'

class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = ['mime_type','url']

class BookDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    book_id = serializers.IntegerField()
    title = serializers.CharField()
    author = serializers.ListField(child=AuthorSerializer())
    # genre = serializers.CharField(default='dummy')  # Placeholder for genre
    language = serializers.ListField(child=LanguageSerializer())
    subjects = serializers.ListField(child=SubjectSerializer())
    bookshelfs = serializers.ListField(child=BookshelfSerializer())
    links = serializers.ListField(child=FormatSerializer())

# class BookDetailSerializer(serializers.ModelSerializer):
#     authors = AuthorSerializer(many=True, source='bookauthors_set')  # Assuming reverse relation
#     bookshelves = BookshelfSerializer(many=True, source='bookbookshelves_set')  # Assuming reverse relation

#     class Meta:
#         model = Book
#         fields = ['id', 'title', 'download_count', 'authors', 'bookshelves']
