from django.urls import path
from .views import BasketSummaryView, BasketAddView

app_name = 'basket'

urlpatterns = [
    path('', BasketSummaryView.as_view(), name='basket_summary'),
    path('add/', BasketAddView.as_view(), name='basket_add'),
]
