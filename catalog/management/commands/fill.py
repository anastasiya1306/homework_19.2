import json
from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        #Удаление данных из таблиц
        Category.objects.all().delete()
        Product.objects.all().delete()

        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            category_data = []
            product_data = []
            for i in data:
                if i['model'] == 'catalog.category':
                    category_data.append(Category(**i['fields']))
                if i['model'] == 'catalog.product':
                    product_data.append(Product(**i['fields']))

        Category.objects.bulk_create(category_data)
        Product.objects.bulk_create(product_data)