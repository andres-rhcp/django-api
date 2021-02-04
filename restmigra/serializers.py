
from rest_framework import serializers 
from restmigra.models import User
 
 
class RestmigraSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ('id',
                  'name',
                  'password')
