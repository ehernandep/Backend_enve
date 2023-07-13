from django.contrib import admin
from .forms import PropertyForm
from .models import Property, PropertyViews


class PropertyAdmin(admin.ModelAdmin):
    list_display = ["title", "country", "advert_type", "property_type"]
    list_filter = ["advert_type", "property_type", "country"]
    form = PropertyForm


admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyViews)