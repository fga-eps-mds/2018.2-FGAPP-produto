from rest_framework import serializers
from product_list.models import ProductList
from django.contrib.auth.models import User

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductList
        fields = '__all__'

<<<<<<< HEAD
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
=======
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')
>>>>>>> 676bccfad4b5683ac66a1afab8b80958691e6bbd
