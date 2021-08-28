from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer


class ProductListView(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()[0:4]

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


class ProductDetailView(APIView):
    def get(self, request, category_slug, product_slug,*args, **kwargs):
        product = get_object_or_404(Product,category__slug=category_slug, slug=product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)