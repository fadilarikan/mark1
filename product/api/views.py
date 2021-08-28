from rest_framework.generics import ListAPIView

from product.api.serializers import ProductSerializer
from product.models import Product
from rest_framework import filters

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']