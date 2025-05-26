from .models import Product, Stock
from rest_framework import serializers

class ProductAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'short_description', 'product_description', 'stock', 'price']

class StockAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['product', 'quantity']
