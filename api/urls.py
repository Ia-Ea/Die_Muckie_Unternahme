from django.urls import path
from .views import ProductAPIView, StockAPIView

urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='products'),
    path('stocks/', StockAPIView.as_view(), name='stocks'),
]
