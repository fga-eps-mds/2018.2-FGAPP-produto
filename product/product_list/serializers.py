from rest_framework import serializers
from product_list.models import ProductList

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductList
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')
