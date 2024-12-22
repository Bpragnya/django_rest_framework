from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .serializers import*
from status_code.status_codes import CustomStatusCodes

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
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        data = list(Book.objects.all().values())
        return Response(data)
    
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
            serializer = self.get_serializer(queryset, many=True)

            return Response({
                "data": serializer.data,
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

