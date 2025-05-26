from django.shortcuts import render

# Create your views here.
from .models import Product, Stock
from rest_framework import generics
from .serializers import ProductAPISerializer, StockAPISerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductAPISerializer
    permission_classes = [AllowAny]

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductAPISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class StockAPIView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockAPISerializer
    permission_classes = [AllowAny]

class StockRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockAPISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

def  home(request):
    return render(request, 'home.html')