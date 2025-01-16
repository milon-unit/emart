from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=58, blank=False, null=False)
    image = models.ImageField(upload_to='category', blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField (auto_now_add=True)
    models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return self.name

    class Meta:
        ordering = ['-created',]
        verbose_name_plural = 'Categories'


class Product (models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    preview_des = models.CharField(max_length=255, verbose_name='Short Descriptions')
    description= models.TextField(max_length=1000, verbose_name='Descriptions')
    image = models.ImageField(upload_to='products', blank=False, null=False)
    price = models.FloatField()
    old_price = models. FloatField(default=8.00, blank=True, null=True)
    is_stock = models.BooleanField(default=True)
    created = models.DateTimeField (auto_now_add=True)

    def _str_(self):
       return self.name

    class Meta:
        ordering = ['-created']


        
