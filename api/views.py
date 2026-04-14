from django.db.models import Max
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from api.serializers import ProductSerializer,OrderSerializer,ProductInfoSerializer,OrderInfoSerializer
from api.models import Product,Order
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.filter(stock__gt=0)
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg= 'product_id'

#Order Lists
class OrderListAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.prefetch_related( 'items','items__product').all()
    serializer_class = OrderSerializer

#Order Details
class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_url_kwarg= 'order_id'

class OrderInfoListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.filter(stock__gt=0)
    serializer = ProductInfoSerializer({
        'products':queryset,
        'count':len(queryset),
        'max_price':queryset.aggregate(max_price=Max('price'))['max_price']
    })


# @api_view(['GET'])
# def product_list(request):
    products= Product.objects.all()
    serializer = ProductInfoSerializer({
        'products':products,
        'count':len(products),
        'max_price':products.aggregate(max_price=Max('price'))['max_price']
    })
#     return Response(serializer.data)