from rest_framework import viewsets
from .models import Vendor
from .serializers import VendorSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    http_method_names = [
        "get",
        "post",
        "put",
        "delete",
    ]