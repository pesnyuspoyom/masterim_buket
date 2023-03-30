from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product
from django.urls import reverse

def home(request):
    return render(request, 'home.html', {'title': 'Мастерим букет'})

def catalog_view(request):
    products = Product.objects.filter(available=True)
    context = {'products': products}
    return render(request, 'catalog.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
