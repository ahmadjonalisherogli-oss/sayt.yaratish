from django.urls import path
from . import views 
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
    path("search/", views.search_products, name="search"),
    path("brand/", views.brand, name="brand"),
]
