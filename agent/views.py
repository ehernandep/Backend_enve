from .serializers import ListingSerializer
from core.models import Listing
from rest_framework.views import APIView
from common.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ListingAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Listing.objects.all()
        serializer = ListingSerializer(queryset, many=True)

        return Response(serializer.data)
