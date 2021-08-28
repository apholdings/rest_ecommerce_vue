from django.urls import path

from .views import ProductListView, ProductDetailView

app_name="shop"

urlpatterns = [
    path('list/', ProductListView.as_view()),
    path('<slug:category_slug>/<slug:product_slug>', ProductDetailView.as_view())
]
