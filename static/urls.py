from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog_view, name='catalog'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
]
