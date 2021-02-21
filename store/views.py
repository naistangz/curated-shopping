from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views.generic import ListView, View, TemplateView


class ProductsView(TemplateView):
    template_name = 'store/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()

        return context


class ProductDetailView(TemplateView):

    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(
            Product, slug=self.kwargs['slug'], in_stock=True)

        context['product'] = product

        return context


class CategoryView(TemplateView):
    template_name = 'store/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category = get_object_or_404(
            Category, slug=self.kwargs['slug'])
        products = Product.objects.filter(category=category)

        context['category'] = category
        context['products'] = products

        return context
