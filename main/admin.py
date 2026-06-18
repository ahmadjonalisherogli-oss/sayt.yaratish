from django.contrib import admin
from .models import Product, Category , Offer

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "is_trending", "is_popular", "is_discounted", "created_at")
    list_filter = ("category", "is_trending", "is_popular", "is_discounted")
    search_fields = ("name", "description")

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "discount", "description", "created_at")
    search_fields = ("title", "category")