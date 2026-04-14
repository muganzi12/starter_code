from django.urls import path
from django.http import HttpResponse
from . import views
# from rest_framework.routers import DefaultRouter


def home(request):
    return HttpResponse("Welcome to RM001 Work Force")

# router = DefaultRouter()
# router.register(r"products", views.ProductViewSet, basename="product")

urlpatterns = [
     path('',home),
     #Get All Products
     path('products/', views.ProductListAPIView.as_view()),
    #  path('products/', views.product_list),

    # path('products/info/', views.product_info),
     #Get Details of One Product
     path('products/<int:product_id>/', views.ProductDetailAPIView.as_view()),
     #path("", include(router.urls)),

     #Get All Orders
     path('orders/', views.OrderListAPIView.as_view()),
     #Get Details of One Order
     path('orders/<uuid:order_id>/', views.OrderDetailAPIView.as_view(), name='order_detail'),
]
