from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import get_home, get_contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', get_home),
    path('contacts/', get_contacts),
]