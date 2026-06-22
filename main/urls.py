from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('product/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path("contact/", views.contact, name="contact"),
    path("women/", views.women, name="women"),
    path("men/", views.men, name="men"),
    path('kids/', views.kids, name='kids'),
    path("accessories/", views.accessories, name="accessories"),
    path("sale/", views.sale, name="sale"),
    path("blog/", views.blog, name="blog"),
    path("groceries/", views.groceries, name="groceries"),
    path("drinks/", views.drinks, name="drinks"),
    path("chocolates/", views.chocolates, name="chocolates"),
    path("brand/", views.brand, name="brand"),
    path("cart/add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart_detail, name="cart_detail"),
    path("login/", auth_views.LoginView.as_view(template_name="main/login.html"), name="login"),
    path("baked-products/", views.baked_products, name="baked_products"),
    path("category/<slug:slug>/", views.category_detail, name="category_detail"),
    path("drinks/", views.drinks, name="drinks"),
]

