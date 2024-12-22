from rest_framework import serializers
from .models import BookAuthors,BookBookshelves,BookLanguages,BookSubjects, Format


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
        fields = '__all__'