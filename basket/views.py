from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DeleteView, UpdateView
from django.http import JsonResponse
from django.views.generic.base import View

from store.models import Product
from .basket import Basket


class BasketSummaryView(TemplateView):
    template_name = 'store/basket/summary.html'


class BasketAddView(TemplateView):

    def post(self, request, *args, **kwargs):
        basket = Basket(request)
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basket_qty = basket.__len__()
        response = JsonResponse({
            'qty': basket_qty,
            'product': product.product_name,
        })
        return response


class BasketDeleteView(DeleteView):

    def post(self, request, *args, **kwargs):
        basket = Basket(request)
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({
            'qty': basketqty,
            'subtotal': baskettotal
        })
        return response


class BasketUpdateView(UpdateView):
    def post(self, request, *args, **kwargs):
        basket = Basket(request)
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({
            'qty':basketqty,
            'subtotal':baskettotal
        })

        return response