from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('secret/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Enve Backend Admin"
admin.site.site_title = "Enve Backend Admin Portal "
admin.site.index_title = "Welcome To Enve"
