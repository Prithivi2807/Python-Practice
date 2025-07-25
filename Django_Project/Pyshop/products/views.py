from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# django -> package shortcuts-> modules importing->render function
# /products -> index
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
         {'products': products})


def new(request):
    return HttpResponse('New Products')

