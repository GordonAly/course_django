from django.urls import path
from .views import products

urlpatterns = [
    path('', products, name='products'),
    path('', products_all, name='все'),
    path('', products_home, name='дом'),
    path('', products_office, name='офис'),
    path('', products_modern, name='модерн'),
    path('', products_classic, name='классика')

]