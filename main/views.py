# from django.shortcuts import render
# from .models import Product , Cart
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views import View
# from django.shortcuts import render, get_object_or_404, redirect
# from django.urls import reverse

# def home_page(request):
#     products = Product.objects.all()
#     return render(request, "main/index.html", {"products": products})

# def product_list(request):
#     products = Product.objects.all()
#     return render(request, "main/product_list.html", {"products": products})

# def product_detail(request, product_slug):
#     product = Product.objects.get(slug=product_slug)
#     return render(request, "main/product_detail.html", {"product": product})

# def category_detail(request, slug):
#     category = Category.objects.get(slug=slug)   
#     products = Product.objects.filter(category=category)
#     return render(request, "main/product_list.html", {"products": products})


# def contact(request):
#     return render(request, "main/contact.html")

# def men(request):
#     products = Product.objects.filter(category__slug="men")
#     return render(request, "main/men.html", {"products": products})

# def women(request):
#     products = Product.objects.filter(category__slug="women") 
#     return render(request, "main/women.html", {"products": products})

# def kids(request):
#     products = Product.objects.filter(category__slug="kids") 
#     return render(request, "main/kids.html", {"products": products})

# def accessories(request):
#     products = Product.objects.filter(category__slug="accessories") 
#     return render(request, "main/accessories.html", {"products": products})

# def sale (request):
#     products = Product.objects.filter(category__slug="sale") 
#     return render(request, "main/sale.html", {"products": products})

# def blog(request):
#     posts = [] 
#     return render(request, "main/blog.html", {"posts": posts})

# def groceries(request):
#     products = Product.objects.filter(category__slug="groceries") 
#     return render(request, "main/groceries.html", {"products": products})

# def drinks(request):
#     products = Product.objects.filter(category__slug="drinks")
#     return render(request, "main/drinks.html", {"products": products})

# def chocolates(request):
#     products = Product.objects.filter(category__slug="chocolates")
#     return render(request, "main/chocolates.html", {"products": products})

# def brand(request):
#     products = Product.objects.filter(category__slug="brand")
#     return render(request, "main/brand.html", {"products": products})

# def search_products(request):
#     query = request.GET.get("q", "")
#     products = Product.objects.filter(name__icontains=query) if query else []
#     return render(request, "main/search_results.html", {"products": products, "query": query})

# def add_to_cart(request, product_id):
#     if not request.user.is_authenticated:
#         login_url = reverse('login')
#         return redirect(f"{login_url}?next={request.path}")

#     product = Product.objects.get(id=product_id)
#     cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()
#     return redirect("cart_detail")


# def cart_detail(request):
#     if not request.user.is_authenticated:
#         login_url = reverse('login')
#         return redirect(f"{login_url}?next={request.path}")
#     cart_items = Cart.objects.filter(user=request.user)
#     return render(request, "main/cart_detail.html", {"cart_items": cart_items})



from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, Category
from django.urls import reverse


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


def sale(request):
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


# --- Pastdagi ikki funksiya XARID bilan bog'liq, shuning uchun login talab qiladi ---

def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        login_url = reverse('login')
        return redirect(f"{login_url}?next={request.path}")

    product = Product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect("cart_detail")


def cart_detail(request):
    if not request.user.is_authenticated:
        login_url = reverse('login')
        return redirect(f"{login_url}?next={request.path}")

    cart_items = Cart.objects.filter(user=request.user)
    return render(request, "main/cart_detail.html", {"cart_items": cart_items})
