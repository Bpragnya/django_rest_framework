from django.db import models
from django.contrib.postgres.indexes import BTreeIndex

# Create your models here.
from books_master.models import Book, Author, Language, Bookshelf, Subject


class BookAuthors(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    book = models.ForeignKey(Book, models.DO_NOTHING) #django automatically adds index for FK relationships.  can disable this by passing db_index=False 
    author = models.ForeignKey(Author, models.DO_NOTHING) #or models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'books_book_authors'
        unique_together = (('book', 'author'),)
        # indexes = BTreeIndex(fields='book_id') #or add specifically for cols


class BookBookshelves(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    book = models.ForeignKey(Book, models.DO_NOTHING)
    bookshelf = models.ForeignKey(Bookshelf, models.DO_NOTHING) #'Bookshelf'

    class Meta:
        db_table = 'books_book_bookshelves'
        unique_together = (('book', 'bookshelf'),)


class BookLanguages(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    book = models.ForeignKey(Book, models.DO_NOTHING)
    language = models.ForeignKey(Language, models.DO_NOTHING)

    class Meta:
        db_table = 'books_book_languages'
        unique_together = (('book', 'language'),)


class BookSubjects(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    book = models.ForeignKey(Book, models.DO_NOTHING)
    subject = models.ForeignKey(Subject, models.DO_NOTHING)

    class Meta:
        db_table = 'books_book_subjects'
        unique_together = (('book', 'subject'),)



class Format(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    mime_type = models.CharField(max_length=32)
    url = models.CharField(max_length=256)
    book = models.ForeignKey(Book, models.DO_NOTHING)

    class Meta:
        db_table = 'books_format'
        # indexes = BTreeIndex(fields='book_id')



