
from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= ['name','product_id','miad','purchase','purchase_date','stock']

