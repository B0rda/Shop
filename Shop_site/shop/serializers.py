from .models import *
from rest_framework import serializers

class AllProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','cathegory','final_price','v_nal']

class AllHozproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = HozProduct
        fields = ['name','cathegory','final_price','v_nal']

class DetailProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class DetailHozproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = HozProduct
        fields = '__all__'
