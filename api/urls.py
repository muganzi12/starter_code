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
     path('products/', views.product_list),

    path('products/info/', views.product_info),
     #Get Details of One Product
     path('products/<int:pk>/', views.product_detail),
     #path("", include(router.urls)),

     #Get All Orders
     path('orders/', views.order_list),
     #Get Details of One Order
     path('orders/<uuid:pk>/', views.order_detail, name='order_detail'),
]
