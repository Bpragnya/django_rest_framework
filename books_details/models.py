from django.db import models
from django.contrib.postgres.indexes import BTreeIndex

# Create your models here.
from books_master.models import Book, Author, Language, Bookshelf, Subject


class BookAuthors(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    book_id = models.ForeignKey(Book, models.DO_NOTHING) #django automatically adds index for FK relationships.  can disable this by passing db_index=False 
    author_id = models.ForeignKey(Author, models.DO_NOTHING) #or models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'books_book_authors'
        unique_together = (('book_id', 'author_id'),)
        # indexes = BTreeIndex(fields='book_id') #or add specifically for cols


class BookBookshelves(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    book_id = models.ForeignKey(Book, models.DO_NOTHING)
    bookshelf_id = models.ForeignKey(Bookshelf, models.DO_NOTHING) #'Bookshelf'

    class Meta:
        db_table = 'books_book_bookshelves'
        unique_together = (('book_id', 'bookshelf_id'),)


class BookLanguages(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    book_id = models.ForeignKey(Book, models.DO_NOTHING)
    language_id = models.ForeignKey(Language, models.DO_NOTHING)

    class Meta:
        db_table = 'books_book_languages'
        unique_together = (('book_id', 'language_id'),)


class BookSubjects(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    book_id = models.ForeignKey(Book, models.DO_NOTHING)
    subject_id = models.ForeignKey(Subject, models.DO_NOTHING)

    class Meta:
        db_table = 'books_book_subjects'
        unique_together = (('book_id', 'subject_id'),)



class Format(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    mime_type = models.CharField(max_length=32)
    url = models.CharField(max_length=256)
    book_id = models.ForeignKey(Book, models.DO_NOTHING)

    class Meta:
        db_table = 'books_format'
        # indexes = BTreeIndex(fields='book_id')



