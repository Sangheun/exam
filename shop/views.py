from django.shortcuts import render
from .models import Category, Shop, Review

def index(request):
    category_list = Category.objects.all()
    return render(request, 'shop/index.html', {
        'category_list': category_list,
        })

def category_new(request):
    pass

