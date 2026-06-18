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


from django.db import models

class Offer(models.Model):
    title = models.CharField(max_length=200)       
    category = models.CharField(max_length=100)    
    description = models.CharField(max_length=200, blank=True, null=True) 
    discount = models.PositiveIntegerField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.category}"
