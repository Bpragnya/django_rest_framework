from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .serializers import*
from rest_framework.decorators import action, api_view
from status_code.status_codes import CustomStatusCodes
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db.models import Prefetch
from django.db.models import Q
from .helpers import *

# Create your views here.

# class BookAuthorsView(viewsets.ModelViewSet):
#     queryset = BookAuthors.objects.all().order_by('id')
#     serializer_class = BookAuthorsSerializer  

#     def create(self, request, *args, **kwargs):
#         try:
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()

#             return Response({
#                 "data": serializer.data,
#                 "message": "Book Author details created successfully",
#                 "statuscode": status.HTTP_201_CREATED
#             }, status=status.HTTP_201_CREATED)

#         except Exception as e:
#             return Response({
#                 "message": "An error occurred.",
#                 "data": str(e),
#                 "statuscode": status.HTTP_500_INTERNAL_SERVER_ERROR
#             }, status=status.HTTP_200_OK)
        
#     def list(self, request, *args, **kwargs):
#         try:
#             queryset = self.get_queryset()
#             # serializer = self.get_serializer(queryset, many=True)
#             page = self.paginate_queryset(queryset)
#             if page is not None:
#                 serializer = self.get_serializer(page, many=True)
#                 result = self.get_paginated_response(serializer.data)
#                 data = result.data # pagination data
#             else:
#                 serializer = self.get_serializer(queryset, many=True)
#                 data = serializer.data

#             return Response({
#                 "data": data,
#                 "message": "Book Author details retrieved successfully",
#                 "statuscode": status.HTTP_200_OK
#             }, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({
#                 "message": "An error occurred.",
#                 "data": str(e),
#                 "statuscode": status.HTTP_500_INTERNAL_SERVER_ERROR
#             }, status=status.HTTP_200_OK)
    
#     def update(self, request, *args, **kwargs):
#         try:
#             instance = self.get_object()
#             serializer = self.get_serializer(instance, data=request.data, partial=True)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()

#             return Response({
#                 "data": serializer.data,
#                 "message": "Book Author details updated succesfully",
#                 "statuscode": status.HTTP_200_OK
#             }, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({
#                 "message": "An error occurred.",
#                 "data": str(e),
#                 "statuscode": status.HTTP_500_INTERNAL_SERVER_ERROR
#             }, status=status.HTTP_200_OK)

#     def destroy(self, request, *args, **kwargs):
#         try:
#             instance = self.get_object()
#             instance.delete()
            
            
#             return Response({
#                 "message": "Book Author deleted successfully",
#                 "statuscode": status.HTTP_200_OK
#             }, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({
#                 "message": "An error occurred.",
#                 "data": str(e),
#                 "statuscode": status.HTTP_500_INTERNAL_SERVER_ERROR
#             }, status=status.HTTP_200_OK)

class BookDetailsView(viewsets.ModelViewSet):
#     queryset = BookAuthors.objects.order_by('-id')[:2]
    serializer_class = BookDetailSerializer

    # @action(detail=False, methods=['get'], url_path=r'custom_books_details/(?P<category_id>\d*)') #suaitable for default minimal params
    @action(detail=False, methods=['get'], url_path=r'custom_books_details')    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_QUERY,
                description="Gutenberg ID",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                'title',
                openapi.IN_QUERY,
                description="Book Title",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                'author',
                openapi.IN_QUERY,
                description="Author",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                'language',
                openapi.IN_QUERY,
                description="Language Code en/fr etc.",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                'mime_type',
                openapi.IN_QUERY,
                description="Mime Type like text/jpeg etc.",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                'topic',
                openapi.IN_QUERY,
                description="Books from relevant Bookshelf or Subject",
                type=openapi.TYPE_STRING,
            ),
        ],
    ) 
    def list_books_details(self, request, *args, **kwargs):      
        try:
            # queryset = self.get_queryset()
            id = request.query_params.get('id')
            title = request.query_params.get('title')            
            author = request.query_params.get('author')
            language = request.query_params.get('language')
            mime_type = request.query_params.get('mime_type')
            topic = request.query_params.get('topic')

            print(f"Values :: id:{id}, title:{title}, author:{author}, language:{language}, mime_type:{mime_type}, topic: {topic}")

            # book_authors =  BookAuthors.objects
            # # book_authors = book_authors.select_related('book','author')
            # # .prefetch_related('book__booklanguages_set')
            # book_authors = book_authors.select_related('book','author').prefetch_related(Prefetch('book', queryset=BookLanguages.objects.select_related('language')))
            # book_authors = book_authors.prefetch_related(Prefetch('book', queryset=BookBookshelves.objects.select_related('bookshelf')))
            # book_authors = book_authors.prefetch_related(Prefetch('book', queryset=BookSubjects.objects.select_related('subject')))
            # book_authors = book_authors.prefetch_related('book__format_set')            

            queryset = Book.objects.select_related().prefetch_related(
            'bookauthors_set__author',  # Prefetch authors related to books
            'booklanguages_set__language',
            'bookbookshelves_set__bookshelf',  # Prefetch bookshelves related to books
            'booksubjects_set__subject',
            'format_set'
            )

            # Applying filters based on provided query parameters
            if id:
                queryset = queryset.filter(gutenberg_id__in=id.split(','))

            if title:
                # queryset = queryset.filter(title__icontains=title)
                titles = title.split(',')  # Assuming comma-separated values for titles
                titles_filters = Q()
                for t in titles:
                    titles_filters |= Q(title__icontains=t)
                #Applying filter for book title
                queryset = queryset.filter(titles_filters)

            queryset = queryset.order_by('-download_count')
            # book_authors = book_authors.distinct().order_by('id') [:10]

            # Print the raw SQL query
            # print(str(queryset.query))     
          
            page = self.paginate_queryset(queryset)
            response_data = []
            if page is not None:
                #serializer response error('Book' object has no attribute 'author'.)
                # serializer = self.get_serializer(page, many=True)
                # result = self.get_paginated_response(serializer.data)
                # ser_data = result.data # pagination data

                for row in page:
                    if author:
                        authors = Helpers.apply_author_filter(row.bookauthors_set,author)
                    else:
                        authors = row.bookauthors_set.all()
                    
                    if language:
                        # queryset = queryset.filter(booklanguages__language__code__in=[lang.strip().lower() for lang in language.split(',')])
                        languages = Helpers.apply_language_filter(row.booklanguages_set,language)
                    else:
                        languages = row.booklanguages_set.all()
                   
                    if topic:
                        subjects = Helpers.apply_subject_filter(row.booksubjects_set,topic)
                        bookshelves = Helpers.apply_bookshelf_filter(row.bookbookshelves_set,topic)
                    else:
                        subjects = row.booksubjects_set.all()
                        bookshelves = row.bookbookshelves_set.all()
                   
                    if mime_type:
                        formats = Helpers.apply_mime_type_filter(row.format_set,mime_type)
                    else:
                        formats = row.format_set.all()
                    
                    response_data.append({
                        "id": row.gutenberg_id,
                        "book_id": row.id,
                        "title": row.title,
                        "author": list({
                            "name": a.author.name,
                            "birth_year": a.author.birth_year,
                            "death_year": a.author.death_year,
                        } for a in authors),
                        # "genre": 'dummy',  # Replace with actual logic if needed
                        "language":list( l.language.code for l in languages),
                        "subjects":list( sub.subject.name for sub in subjects),
                        "bookshelfs":list( bs.bookshelf.name for bs in bookshelves),
                        "links": list({"mime_type": f.mime_type, "url": f.url } for f in formats),
                    })
                result = self.get_paginated_response(response_data)
                data = result.data # pagination data
            else:
                #ser response
                # serializer = self.get_serializer(books, many=True)
                # ser_data = serializer.data 
                # custon response         
                data = response_data   
           
            return Response({
                "data": data,
                "message": "Books details retrieved successfully",
                "statuscode": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": "An error occurred.",
                "data": str(e),
                "statuscode": status.HTTP_500_INTERNAL_SERVER_ERROR
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   