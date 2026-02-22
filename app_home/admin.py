from django.contrib import admin
from django.utils.html import format_html

from .models import PageCategory, Page, Map


@admin.register(PageCategory)
class PageCategoryAdmin(admin.ModelAdmin):
    """ Админка для категорий универсальных страниц """
    list_display = ('name', 'parent', 'description', 'image')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('parent',)
    ordering = ('name',)

class MapInline(admin.TabularInline):
    """ Встроенные карты в записи page """
    model = Map
    extra = 0
    fields = ('name', 'latitude', 'longitude', 'description', 'drag', 'scroll', 'zoom')
    show_change_link = True

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """ Админка для категорий универсальных страниц """
    list_display = (
        'name', 'slug', 'subtitle','image_preview', 'category', 'is_active', 'is_checked', 'created_at', 'updated_at',
    )
    readonly_fields = ('created_at', 'views')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('category', 'is_active', 'is_checked', 'created_at', 'updated_at',)
    ordering = ('name',)
    inlines = [MapInline]

    def image_preview(self, obj):
        """ Показывает миниатюру в списке и карточке товара """
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 6px;" />',
                obj.image.url
            )
        return '—'
    image_preview.short_description = 'Превью'
