from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from django.urls import reverse


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Category(models.Model):
    category_choices = (
        ('tech', 'Technology'),
        ('accessories', 'Accessories'),
        ('books', 'Books'),
        ('jewellery', 'Jewellery')
    )

    category_name = models.CharField(
        max_length=255, choices=category_choices)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('store:category_list', kwargs={'slug': self.slug})


class Product(models.Model):

    CURRENCY_CHOICES = (
        ('EUR', 'EUR'),
        ('USD', 'USD'),
        ('GBP', 'GBP')
    )
    CURRENCY_DEFAULT = 'GBP'
    category = models.ForeignKey(
        Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='product_creater')
    product_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    slug = models.SlugField(max_length=255)
    price = MoneyField(max_digits=6, decimal_places=2,
                       currency_choices=CURRENCY_CHOICES, default_currency=CURRENCY_DEFAULT)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('store:product_detail', kwargs={'slug': self.slug})
