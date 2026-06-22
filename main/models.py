from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)   
    slug = models.SlugField(unique=True)      

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)   
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    description = models.TextField(blank=True, null=True)         
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    is_trending = models.BooleanField(default=False)   
    is_popular = models.BooleanField(default=False)    
    is_discounted = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Promotion(models.Model):
    title = models.CharField(max_length=200)
    discount_percent = models.PositiveIntegerField()
    image = models.ImageField(upload_to="promotions/")
    link = models.CharField(max_length=200, blank=True, default="#")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.discount_percent}% - {self.title}"

