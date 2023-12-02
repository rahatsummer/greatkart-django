from django.db import models
from django.urls import reverse
from category.models import Category
from accounts.models import Account


# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    # create these two properties additional based on our
    # custom user model

    created_by = models.ForeignKey(
        Account, related_name='created_products', on_delete=models.SET_NULL, null=True, editable=False)
    modified_by = models.ForeignKey(
        Account, related_name='modified_products', on_delete=models.SET_NULL, null=True, editable=False)

    # The reverse function is used to generate a URL for a given view
    # The arguments passed to reverse are [self.category.slug, self.slug].
    # It seems like this URL pattern expects two parameters:
    # the slug of the category and the slug of the product.
    # These slugs are likely used to uniquely identify the category and product
    # in the URL
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name
