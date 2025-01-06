from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'books_details', BookAuthorsView, basename='books_details')
router.register(r'books_detail_view', BookDetailsView, basename='books_details')

# urlpatterns = [
#     path('', include(router.urls)),
# ]
urlpatterns = router.urls

