
from rest_framework import serializers 
from restmigra.models import Product
 
 
class RestmigraSerializer(serializers.ModelSerializer):
 
   
    class Meta:
        model = Product
        fields = ('product_sku',
                  'product_name',
                  'product_type',
                  'stock',
                  'date_update',
                  'user_update',
                  'observation')
