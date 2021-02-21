from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.http import JsonResponse

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
        basket.add(product=product, product_qty)
        response = JsonResponse({'test': 'data'})
        return response
