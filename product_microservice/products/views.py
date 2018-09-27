from products.models import Product
from products.serializers import ProductSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.response import Response
import requests

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(["POST"])
def delete_product(request):
    # If request is valid
    fk_vendor = request.data.get("fk_vendor")
    product_id = request.data.get("product_id")
    if (product_id == None or fk_vendor == None):
        return Response({'error': 'Formulário inválido.'},
                                status=HTTP_400_BAD_REQUEST)
    # If product exist
    try:
        product = Product.objects.get(id=product_id)
    except:
        return Response({'error': 'Produto não existe.'},
                                status=HTTP_404_NOT_FOUND)
    # If user is owner of product
    if (int(fk_vendor) == product.fk_vendor):
        product.delete()
        return Response(status=HTTP_200_OK)
    return Response({'error': 'Produto não pertence a este usuário, permissão negada.'},
                            status=HTTP_403_FORBIDDEN)

@api_view(["POST"])
def create_product(request):
    fk_vendor = request.data.get("fk_vendor")
    name = request.data.get("name")
    price = 0.0
    try:
        price = float(request.data.get("price"))
    except:
        return Response({'error': 'Campo inválido de preço.'},
                                status=HTTP_400_BAD_REQUEST)
    photo = request.data.get("photo")
    description = request.data.get("description")

    # verifying if request is valid
    if (fk_vendor == None or name == None or name == "" or price == 0.0 or photo == None or description == None or description == ""):
        return Response({'error': 'Um ou mais campos vazios.'},
                                status=HTTP_400_BAD_REQUEST)

    Product.objects.create(
                        fk_vendor = fk_vendor,
                        name = name,
                        price = price,
                        photo = photo,
                        description = description)

    return Response(status=HTTP_200_OK)
