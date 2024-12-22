from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('user', UserView, basename='user')
router.register('books_master', BookView, basename='books_master')


urlpatterns = router.urls

