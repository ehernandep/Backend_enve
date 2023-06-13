
from django.contrib import admin
from django.urls import path, include
from listings.api import views as listings_api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/listings/', listings_api_views.ListingList.as_view()),
    path('api/admin/',include('administrator.urls'))
]
