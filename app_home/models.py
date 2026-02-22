import os
from django.db import models
from django.utils.text import slugify


def page_image_path(instance, filename):
    """ Функция создания пути для картинок страниц """
    return os.path.join('pages', instance.slug or 'temp', filename)

class PageCategory(models.Model):
    """ Модель категории универсальных страниц """
    name = models.CharField(max_length=100, verbose_name='Название категории')
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name='Алиас')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to=page_image_path, null=True, blank=True, verbose_name='Изображение')
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children', verbose_name='Родительская категория',
    )

    class Meta:
        verbose_name = "Категория страниц"
        verbose_name_plural = "Категории страниц"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while PageCategory.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Page(models.Model):
    """ Модель универсальных страниц """
    name = models.CharField(max_length=250, verbose_name='Название')
    subtitle = models.CharField(max_length=250, unique=True, blank=True, verbose_name='Подзаголовок')
    slug = models.SlugField(max_length=250, unique=True, blank=True, verbose_name='Алиас')
    short_description = models.TextField(null=True, blank=True, verbose_name='Краткое описание')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    views = models.IntegerField(default=0, blank=True, verbose_name='Просмотры')
    category = models.ForeignKey(PageCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Категория')
    is_active = models.BooleanField(default=True, blank=True, verbose_name='Активен')
    is_checked = models.BooleanField(default=False, blank=True, verbose_name='Выбран')
    image = models.ImageField(upload_to=page_image_path, null=True, blank=True, verbose_name='Изображение')
    icon = models.TextField(null=True, blank=True, verbose_name='Иконка SVG')
    link = models.URLField(max_length=500, null=True, blank=True, verbose_name='Прикрепленная ссылка')
    number = models.IntegerField(default=0, blank=True, verbose_name='Количество')
    seo_title = models.CharField(max_length=250, null=True, blank=True, verbose_name='Название для SEO')
    seo_keywords = models.CharField(max_length=500, null=True, blank=True, verbose_name='Ключевики для SEO')
    seo_description = models.TextField(null=True, blank=True, verbose_name='SEO описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Page.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Map(models.Model):
    """ Модель Яндекс карты """
    name = models.CharField(max_length=250, verbose_name='Название')
    latitude = models.CharField(max_length=100, null=True, blank=True, verbose_name='Широта')
    longitude = models.CharField(max_length=100, null=True, blank=True, verbose_name='Долгота')
    description = models.CharField(max_length=100, null=True, blank=True, verbose_name='Адрес точки')
    drag = models.BooleanField(default=True, blank=True, verbose_name='Перетаскивание карты')
    scroll = models.BooleanField(default=True, blank=True, verbose_name='Прокрутка карты')
    zoom = models.IntegerField(default=15, blank=True, verbose_name='Масштаб карты')
    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True, blank=True, related_name='map', verbose_name='Страница')

    class Meta:
        verbose_name = "Карта"
        verbose_name_plural = "Карты"

    def __str__(self):
        return self.name
