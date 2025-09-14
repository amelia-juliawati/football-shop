from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product

def show_main(request):
    products_list = Product.objects.all()
    
    context = {
        'nama_toko' : 'Turboa Shop',
        'nama': 'Amelia Juliawati',
        'npm' : '2406414076',
        'kelas' : 'PBP A',
        'products_list' : products_list
    }

    return render(request, "main.html", context)

def create_products(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    context = {'form': form}
    return render(request, "create_products.html", context)

def show_products(request, id):
    products = get_object_or_404(Product, pk = id)
    context = {
        'products': products
    }
    return render(request, "products_detail.html", context)

def show_xml(request):
     products_list = Product.objects.all()
     xml_data = serializers.serialize("xml", products_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, products_id):
    try:
        products_item = Product.objects.filter(pk=products_id)
        xml_data = serializers.serialize("xml", products_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, products_id):
    try:
        products_item = Product.objects.get(pk=products_id)
        json_data = serializers.serialize("json", [products_item])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)