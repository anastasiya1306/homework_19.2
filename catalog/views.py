from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Blog


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Главная'
    }


def get_contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return context_data


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Статьи'
    }

    def get_queryset(self):
        """Выводит список статей с положительным признаком публикации"""
        queryset = super().get_queryset()
        queryset = queryset.filter(is_publication=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return context_data

    def get_object(self, **kwargs):
        views = super().get_object(**kwargs)
        views.count_views += 1
        views.save()
        return views


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'description', 'preview', 'is_publication')
    success_url = reverse_lazy('main:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'description', 'preview', 'is_publication')

    def get_success_url(self):
        return reverse('main:blog_item', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('main:blog_list')