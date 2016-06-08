from .forms import CategoryForm
from django.shortcuts import render, get_object_or_404
from .models import Category, Shop, Review
from django.shortcuts import render

def index(request):
    category_list = Category.objects.all()
    return render(request, 'shop/index.html', {
        'category_list': category_list,
        })


def category_new(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('shop:category_detail', category_pk)
    else:
        form = CategoryForm()
    return render(request, 'blog/category_form.html', {
        'form':form,
        })


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'shop/category_detail.html', {
        'category':category,
        })