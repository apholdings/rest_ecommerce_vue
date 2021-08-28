from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.db.models import Q

from django.shortcuts import get_object_or_404

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


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


class CategoryDetailView(APIView):
    def get(self, request, category_slug,*args, **kwargs):
        category = get_object_or_404(Category, slug=category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    query=request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products":[]})