from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import get_home, get_contacts, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', get_home, name='home'),
    path('contacts/', get_contacts, name='contacts'),
    path('product_card/<int:pk>/', product, name='product_item')
]