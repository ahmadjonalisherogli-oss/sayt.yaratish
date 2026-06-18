from django.shortcuts import render
from .models import Product , Offer

def home_page(request):
    products = Product.objects.all()
    return render(request, "main/index.html", {"products": products})

def product_list(request):
    products = Product.objects.all()
    return render(request, "main/product_list.html", {"products": products})

def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    return render(request, "main/product_detail.html", {"product": product})

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)   
    products = Product.objects.filter(category=category)
    return render(request, "main/product_list.html", {"products": products})

def home_page(request):
    offers = Offer.objects.all()
    return render(request, "main/index.html", {"offers": offers})

def contact(request):
    return render(request, "main/contact.html")

def men(request):
    products = Product.objects.filter(category__slug="men")
    return render(request, "main/men.html", {"products": products})

def women(request):
    products = Product.objects.filter(category__slug="women") 
    return render(request, "main/women.html", {"products": products})

def kids(request):
    products = Product.objects.filter(category__slug="kids") 
    return render(request, "main/kids.html", {"products": products})

def accessories(request):
    products = Product.objects.filter(category__slug="accessories") 
    return render(request, "main/accessories.html", {"products": products})

def sale (request):
    products = Product.objects.filter(category__slug="sale") 
    return render(request, "main/sale.html", {"products": products})

def blog(request):
    posts = [] 
    return render(request, "main/blog.html", {"posts": posts})

def groceries(request):
    products = Product.objects.filter(category__slug="groceries") 
    return render(request, "main/groceries.html", {"products": products})

def drinks(request):
    products = Product.objects.filter(category__slug="drinks")
    return render(request, "main/drinks.html", {"products": products})

def chocolates(request):
    products = Product.objects.filter(category__slug="chocolates")
    return render(request, "main/chocolates.html", {"products": products})

def brand(request):
    products = Product.objects.filter(category__slug="brand")
    return render(request, "main/brand.html", {"products": products})

def search_products(request):
    query = request.GET.get("q", "")
    products = Product.objects.filter(name__icontains=query) if query else []
    return render(request, "main/search_results.html", {"products": products, "query": query})
