
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/admin/',include('administrator.urls')),
     path('api/agent/',include('agent.urls'))
]
