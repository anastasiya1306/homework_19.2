from django.contrib import admin

from catalog.models import Product, Category, Blog


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    search_fields = ('name', 'description',)
    list_filter = ('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'description', 'preview')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}