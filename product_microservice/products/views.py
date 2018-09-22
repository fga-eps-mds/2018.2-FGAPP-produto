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
        return Response({'error': 'Formulario invalido.'},
                                status=HTTP_400_BAD_REQUEST)
    # If product exist
    try:
        product = Product.objects.get(id=product_id)
    except:
        return Response({'error': 'Produto nao existe.'},
                                status=HTTP_404_NOT_FOUND)
    # If user is owner of product
    if (int(fk_vendor) == product.fk_vendor):
        product.delete()
        return Response(status=HTTP_200_OK)
    return Response({'error': 'Produto nao pertence a este usuario, permissao negada.'},
                            status=HTTP_403_FORBIDDEN)
