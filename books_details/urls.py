from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books_details', BookAuthorsView, basename='books_details')


urlpatterns = router.urls

