from django.urls import path
from .views import ProductsView, CategoryView, ProductDetailView

app_name = 'store'

urlpatterns = [
    path('', ProductsView.as_view(), name='all_products'),
    path('item/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('shop/<slug:slug>/',
         CategoryView.as_view(), name='category_list'),

]
