from django.shortcuts import render

from catalog.models import Product


def get_home(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/home.html', context)

def get_contacts(request):
    return render(request, 'catalog/contacts.html')

def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object': product_item,
        'title': product_item,
    }
    return render(request, 'catalog/product_card.html', context)