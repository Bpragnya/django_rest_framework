from django.db import models
# from django.db.models import CheckConstraint, Q

# Create your models here.
# class User(models.Model):
#     id = models.IntegerField(primary_key=True, editable=False)
#     name = models.CharField(max_length=250)
#     email = models.CharField(max_length=250)

class Author(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    birth_year = models.SmallIntegerField(blank=True, null=True)
    death_year = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)

    class Meta:
        # managed = False # Default True for creating table while migartion and managing CRUD ops
        db_table = 'books_author'
        


class Book(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    download_count = models.IntegerField(blank=True, null=True)
    gutenberg_id = models.IntegerField(unique=True)
    media_type = models.CharField(max_length=16)
    title = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        db_table = 'books_book'
        # constraint = [CheckConstraint(check=Q(download_count__gte=0), name="books_book_download_count_check"),
        #               CheckConstraint(check=Q(gutenberg_id__gte=0), name="books_book_gutenberg_id_check")
        #               ]


class Bookshelf(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        db_table = 'books_bookshelf'

class Language(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    code = models.CharField(unique=True, max_length=4)

    class Meta:
        db_table = 'books_language'


class Subject(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'books_subject'

        



