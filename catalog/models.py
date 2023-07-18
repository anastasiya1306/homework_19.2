from transliterate import translit
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    ACTIV = 'Активна'
    NO_ACTIV = 'Не активна'

    SELECT_STATUS = [
        (ACTIV, 'Активна'),
        (NO_ACTIV, 'Не активна'),
    ]

    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='images/', verbose_name='Изображение', **NULLABLE)
    category = models.CharField(max_length=150, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    date_creation = models.DateField(verbose_name='Дата создания')
    date_modified = models.DateField(verbose_name='Дата последнего изменения')
    user = models.CharField(max_length=50, verbose_name='Автор', **NULLABLE)
    status = models.CharField(max_length=50, default=NO_ACTIV, choices=SELECT_STATUS, verbose_name='Статус')


    def __str__(self):
        return f'{self.name} {self.description} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)
        permissions = [
            (
                'set_published_product',
                'Can publish product'
            ),
            (
                'change_description_product',
                'Can change description'
            ),
            (
                'change_category_product',
                'Can change category product'
            )
        ]


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='URL', unique=True, db_index=True)
    description = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blogs/', verbose_name='Изображение', **NULLABLE)
    date_creation = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_publication = models.BooleanField(default=True, verbose_name='Признак публикации')
    count_views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Преобразование заголовка в slug"""
        if not self.slug:
            # Транслитерация заголовка статьи с русского на английский
            title_translate = translit(self.title, 'ru', reversed=True)
            self.slug = slugify(title_translate, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.CharField(max_length=150, verbose_name='Номер версии')
    name_version = models.CharField(max_length=150, verbose_name='Название версии')
    is_active = models.BooleanField(default=True, verbose_name='Признак текущей версии')

    def __str__(self):
        return self.name_version

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
