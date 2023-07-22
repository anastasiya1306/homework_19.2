from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import get_contacts, ProductListView, ProductDetailView, BlogListView, BlogDetailView, \
    BlogCreateView, BlogUpdateView, BlogDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    VersionListView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', get_contacts, name='contacts'),
    path('product_detail/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_item'),
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_item'),
    path('blogs/create/', never_cache(BlogCreateView.as_view()), name='blog_create'),
    path('blogs/update/<int:pk>/', never_cache(BlogUpdateView.as_view()), name='blog_update'),
    path('blogs/delete/<int:pk>/', never_cache(BlogDeleteView.as_view()), name='blog_delete'),
    path('products/create/', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('products/update/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='product_update'),
    path('products/delete/<int:pk>/', never_cache(ProductDeleteView.as_view()), name='product_delete'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
]
