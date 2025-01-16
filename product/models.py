from django.db import models
from datetime import datetime
# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=58, blank=False, null=False)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='category', blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField (auto_now_add=True)

    def _str_(self):
        return self.name

    class Meta:
        ordering = ['-created',]
        verbose_name_plural = 'Categories'

class Product (models.Model):
      category = models.ForeignKey(Category,related_name='products', on_delete=models.CASCADE)
      image = models.ImageField(upload_to='product',blank=True,null=True)
      name = models.CharField(max_length=58, blank=False, null=False)
      slug = models.SlugField(max_length=58, blank=False, null=False)
      description = models.TextField(blank=True)
      price = models.DecimalField(max_digits=10,decimal_places=2)
      created = models.DateTimeField(auto_now_add=True)
      updated = models.DateTimeField(auto_now=True)
      def _str_(self):
          return self.name
      def get_absolute_url(self):
        return reverse('products:product_detail',kwargs={'id':self.id, 'slug':self.slug})
      class Meta:
        ordering = ['-created']
