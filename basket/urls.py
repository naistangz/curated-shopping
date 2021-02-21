from django.urls import path
from .views import BasketSummaryView

app_name = 'basket'

urlpatterns = [
    path('', BasketSummaryView.as_view(), name='basket_summary'),
]
