from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .serializers import*
from status_code.status_codes import CustomStatusCodes
# from djangoproject.pagination import CustomPagination
# from rest_framework.pagination import PageNumberPagination

# Create your views here.


# class UserView(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def list(self, request, *args, **kwargs):
#         data = list(User.objects.all().values())
#         return Response(data)

#     def retrieve(self, request, *args, **kwargs):
#         data = list(User.objects.filter(id=kwargs['pk']).values())
#         return Response(data)

#     def create(self, request, *args, **kwargs):
#         user_serializer_data = UserSerializer(data=request.data)
#         if user_serializer_data.is_valid():
#             user_serializer_data.save()
#             status_code = status.HTTP_201_CREATED
#             return Response({"message": "User Added Sucessfully", "status": status_code, "data": user_serializer_data})
#         else:
#             status_code = status.HTTP_400_BAD_REQUEST
#             return Response({"message": "please fill the details", "status": status_code,  "data": user_serializer_data})

#     def destroy(self, request, *args, **kwargs):
#         user_data = User.objects.filter(id=kwargs['pk'])
#         if user_data:
#             user_data.delete()
#             status_code = status.HTTP_201_CREATED
#             return Response({"message": "User delete Sucessfully", "status": status_code})
#         else:
#             status_code = status.HTTP_400_BAD_REQUEST
#             return Response({"message": "User data not found", "status": status_code})

#     def update(self, request, *args, **kwargs):
#         user_details = User.objects.get(id=kwargs['pk'])
#         user_serializer_data = UserSerializer(
#             user_details, data=request.data, partial=True)
#         if user_serializer_data.is_valid():
#             user_serializer_data.save()
#             status_code = status.HTTP_201_CREATED
#             return Response({"message": "User Update Sucessfully", "status": status_code,  "data": user_serializer_data})
#         else:
#             status_code = status.HTTP_400_BAD_REQUEST
#             return Response({"message": "User data Not found", "status": status_code})

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    # queryset = Book.objects.all().order_by('-id')[:20]
    serializer_class = BookSerializer
    # pagination_class = CustomPagination or set globally in settings.py
    # pagination_class = PageNumberPagination
    # pagination_class.page_size = 2
    # pagination_class.page_size_query_param = 'page_size'
    # pagination_class.max_page_size = 10
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                "data": serializer.data,
                "message": "Book created successfully",
                "statuscode": CustomStatusCodes.SUCCESS
            }, status=CustomStatusCodes.SUCCESS)

        except Exception as e:
            return Response({
                "message": "An error occurred.",
                "data": str(e),
                "statuscode": CustomStatusCodes.INTERNAL_SERVER_ERROR
            }, status=CustomStatusCodes.SUCCESS)
        
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
                "message": "Book details retrieved successfully",
                "statuscode": CustomStatusCodes.SUCCESS
            }, status=CustomStatusCodes.SUCCESS)

        except Exception as e:
            return Response({
                "message": "An error occurred.",
                "data": str(e),
                "statuscode": CustomStatusCodes.INTERNAL_SERVER_ERROR
            }, status=CustomStatusCodes.SUCCESS)
    
    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                "data": serializer.data,
                "message": "Book details updated succesfully",
                "statuscode": CustomStatusCodes.SUCCESS
            }, status=CustomStatusCodes.SUCCESS)

        except Exception as e:
            return Response({
                "message": "An error occurred.",
                "data": str(e),
                "statuscode": CustomStatusCodes.INTERNAL_SERVER_ERROR
            }, status=CustomStatusCodes.SUCCESS)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            
            
            return Response({
                "message": "Book deleted successfully",
                "statuscode": CustomStatusCodes.SUCCESS
            }, status=CustomStatusCodes.SUCCESS)

        except Exception as e:
            return Response({
                "message": "An error occurred.",
                "data": str(e),
                "statuscode": CustomStatusCodes.INTERNAL_SERVER_ERROR
            }, status=CustomStatusCodes.SUCCESS)

