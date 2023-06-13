from django.urls import path, include
from .views import ListingAPIView

urlpatterns = [
    path('', include('common.urls')),
    path('listings', ListingAPIView.as_view()),

]