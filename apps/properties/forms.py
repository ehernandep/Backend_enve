from django import forms
from .models import Property
from django.contrib.gis.geos import Point


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            "user",
            "title",
            "ref_code",
            "description",
            "country",
            "city",
            "postal_code",
            "street_address",
            "property_number",
            "price",
            "tax",
            "plot_area",
            "total_floors",
            "bedrooms",
            "bathrooms",
            "advert_type",
            "property_type",
            "cover_photo",
            "photo1",
            "photo2",
            "photo3",
            "photo4",
            "published_status",
            "views",
            "location",
            "latitude",
            "longitude",
        ]

    latitude = forms.FloatField()
    longitude = forms.FloatField()

    def clean(self):
        data = super().clean()
        latitude = data.pop("latitude")
        longitude = data.pop("longitude")
        data["location"] = Point(latitude, longitude, srid=4326)
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        location = self.initial.get("location")
        if isinstance(location, Point):
            self.initial["latitude"] = location.tuple[0]
            self.initial["longitude"] = location.tuple[1]
