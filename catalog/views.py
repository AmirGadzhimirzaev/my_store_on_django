from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


def products_list(request):
    products_l = Product.objects.all()
    context = {'products_l': products_l}
    return render(request, 'products_list.html', context)


def products_details(request, pk):
    products_d = get_object_or_404(Product, pk=pk)
    contex = {"products_d": products_d}
    return render(request, 'products_detail.html', contex)
