from django.db.models import Max
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from api.serializers import ProductSerializer,OrderSerializer,ProductInfoSerializer,OrderInfoSerializer
from api.models import Product,Order
from rest_framework.response import Response
from rest_framework.decorators import api_view

#Product Lists
@api_view(['GET'])
def product_list(request):
    products= Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
#Product Details
@api_view(['GET'])
def product_detail(request,pk):
    product= get_object_or_404(Product,pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#Order Lists
@api_view(['GET'])
def order_list(request):
    orders= Order.objects.all()
    # serializer = OrderSerializer(orders, many=True)
    serializer = OrderInfoSerializer({
        'orders':orders,
        'count':len(orders),
    })
    return Response(serializer.data)
#Order Details
@api_view(['GET'])
def order_detail(request,pk):
    order= get_object_or_404(Order,pk=pk)
    serializer = OrderSerializer(order)
    return Response(serializer.data)

@api_view(['GET'])
def product_info(request):
    products= Product.objects.all()
    serializer = ProductInfoSerializer({
        'products':products,
        'count':len(products),
        'max_price':products.aggregate(max_price=Max('price'))['max_price']
    })
    return Response(serializer.data)