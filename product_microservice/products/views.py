from products.models import Product
from products.serializers import ProductSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from rest_framework.response import Response

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(["POST"])
def ProductDelete(request):
    fk_vendor = request.data.get("fk_vendor")
    try:
        product = Product.objects.get(id=request.data.get("product_id"))
    except:
        return Response({'error': 'Produto nao existe.'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)

    if (int(fk_vendor) == product.fk_vendor):
        product.delete()
        return Response(status=HTTP_200_OK)

    return Response({'error': 'Produto nao pertence a este usuario, permissao negada.'},
                            status=HTTP_403_FORBIDDEN)
