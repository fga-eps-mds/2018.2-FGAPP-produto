from django.shortcuts import render
from product_list.models import ProductList
from product_list.serializers import ProductListSerializer

from rest_framework import generics

class ProductListCreate(generics.ListCreateAPIView):
    queryset = ProductList.objects.all()
    serializer_class = ProductListSerializer


# Create your views here.
