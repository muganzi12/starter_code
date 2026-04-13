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
     path('products/', views.product_list),
       path('products/<int:pk>/', views.product_detail),
    #  path("", include(router.urls)),
]
