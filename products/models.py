from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    slug = models.CharField(max_length = 255)
    icon_url = models.CharField(max_length = 255, null = True)
    
    created_at =  models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now = True)
    deleted_at = models.DateTimeField(null=True)
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 255)
    unit = models.CharField(max_length = 3)
    price = models.FloatField()
    discount = models.IntegerField()
    amount = models.IntegerField()
    is_public = models.BooleanField()
    thumbnail = models.CharField(max_length = 128)
    category_id = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'products', null = False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

class Meta:
    ordering = ['-created_at']
    indexes = [models.Index(fields=['created_at'])]
    
class ProductImage(models.Model):
    id = models.AutoField(primary_key=True)
    image_url = models.CharField(max_length=128)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images', null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    
class ProductComment(models.Model):
    id = models.AutoField(primary_key=True)
    rating = models.IntegerField()
    comment = models.CharField(max_length=512)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_comments', null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)





