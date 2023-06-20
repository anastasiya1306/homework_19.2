from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import get_contacts, ProductListView, ProductDetailView, BlogListView, BlogDetailView, \
    BlogCreateView, BlogUpdateView, BlogDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    VersionListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', get_contacts, name='contacts'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_item'),
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_item'),
    path('blogs/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blogs/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blogs/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]
