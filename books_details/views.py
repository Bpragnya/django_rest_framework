from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .serializers import*

# Create your views here.

class BookAuthorsView(viewsets.ModelViewSet):
    queryset = BookAuthors.objects.all()
    serializer_class = BookAuthorsSerializer

    def list(self, request, *args, **kwargs):
        data = list(BookAuthors.objects.all().values())
        return Response(data)
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                "data": serializer.data,
                "message": "Book Author details created successfully",
                "statuscode": status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                "message": "An error occurred.",
                "data": str(e),
                "statuscode": status.HTTP_500_INTERNAL_SERVER_ERROR
            }, status=status.HTTP_200_OK)
        
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            # serializer = self.get_serializer(queryset, many=True)
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                result = self.get_paginated_response(serializer.data)
                data = result.data # pagination data
            else:
                serializer = self.get_serializer(queryset, many=True)
                data = serializer.data

            return Response({
                "data": data,
                "message": "Book Author details retrieved successfully",
                "statuscode": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": "An error occurred.",
                "data": str(e),
                "statuscode": status.HTTP_500_INTERNAL_SERVER_ERROR
            }, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                "data": serializer.data,
                "message": "Book Author details updated succesfully",
                "statuscode": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": "An error occurred.",
                "data": str(e),
                "statuscode": status.HTTP_500_INTERNAL_SERVER_ERROR
            }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            
            
            return Response({
                "message": "Book Author deleted successfully",
                "statuscode": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": "An error occurred.",
                "data": str(e),
                "statuscode": status.HTTP_500_INTERNAL_SERVER_ERROR
            }, status=status.HTTP_200_OK)

