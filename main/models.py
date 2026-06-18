from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)   # Kategoriya nomi
    slug = models.SlugField(unique=True)      # URL uchun slug

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)   # Mahsulot nomi
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Narx
    description = models.TextField(blank=True, null=True)         # Tavsif
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    is_trending = models.BooleanField(default=False)   # Trenddagi mahsulot
    is_popular = models.BooleanField(default=False)    # Mashhur mahsulot
    is_discounted = models.BooleanField(default=False) # Chegirmadagi mahsulot
    created_at = models.DateTimeField(auto_now_add=True) # Qo‘shilgan vaqt

    def __str__(self):
        return self.name


from django.db import models

class Offer(models.Model):
    title = models.CharField(max_length=200)       # Masalan: "20% off"
    category = models.CharField(max_length=100)    # Masalan: "Fruits & Vegetables"
    description = models.CharField(max_length=200, blank=True, null=True)  # Masalan: "Shop Collection"
    discount = models.PositiveIntegerField(default=0)  # Foiz chegirma (20, 15 va h.k.)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.category}"
