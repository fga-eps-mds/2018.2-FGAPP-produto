from django.shortcuts import render
from product_list.models import ProductList
from product_list.serializers import ProductListSerializer, UserSerializer
from django.contrib.auth.models import User

from rest_framework import generics

class ProductListCreate(generics.ListCreateAPIView):
    queryset = ProductList.objects.all()
    serializer_class = ProductListSerializer

class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
