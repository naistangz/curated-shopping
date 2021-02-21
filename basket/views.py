from django.shortcuts import render
from django.views.generic import TemplateView


class BasketSummaryView(TemplateView):
    template_name = 'store/basket/summary.html'
