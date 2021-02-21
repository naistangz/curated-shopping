from django.shortcuts import render
from django.views.generic import TemplateView


class BasketSummaryView(TemplateView):
    template_name = 'store/basket/summary.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['products'] = Product.objects.all()

    #     return context
