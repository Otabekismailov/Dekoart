from django.contrib import admin

from apps.products.models import *
from modeltranslation.admin import TranslationAdmin


class CategoryAdmin(TranslationAdmin):
    list_display = [
        'id',
        'name',
    ]


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(TranslationAdmin):
    list_display = [
        'id',
        'name',
        'views_count',
        'photo_url',
        'video_url',
    ]


admin.site.register(Product, ProductAdmin)


class FigureOutAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'product',
        'photo_url',
    ]


admin.site.register(FigureOut, FigureOutAdmin)


class ColorCatalogAdmin(TranslationAdmin):
    list_display = [
        'id',
        'product',
        'name',
        'photo_url',
    ]


admin.site.register(ColorCatalog, ColorCatalogAdmin)


class NewsAdmin(TranslationAdmin):
    list_display = [
        'id',
        'title',
        'views_count',
    ]


admin.site.register(News, NewsAdmin)


class Attachment_NewsAdmin(TranslationAdmin):
    list_display = [
        'id',
        'news',
        'title',
        'photo_url',
    ]


admin.site.register(Attachment_News, Attachment_NewsAdmin)


class VideosAdmin(TranslationAdmin):
    list_display = [
        'id',
        'title',
        'views_count',
        'photo_url',
        'video_url',
    ]


admin.site.register(Videos, VideosAdmin)


class MastersAdmin(TranslationAdmin):
    list_display = [
        'id',
        'name',
        'views_count',
    ]


admin.site.register(Masters, MastersAdmin)


class Attachment_MastersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'master',
        'photo_url',
    ]


admin.site.register(Attachment_Masters, Attachment_MastersAdmin)


class ServicesTypeAdmin(TranslationAdmin):
    list_display = [
        'id',
        'name',
    ]


admin.site.register(ServicesType, ServicesTypeAdmin)


class ServicesAdmin(TranslationAdmin):
    list_display = [
        'id',
        'type',
        'name',
        'views_count',
    ]


admin.site.register(Services, ServicesAdmin)


class AttachmentServicesAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'service',
        'photo_url',
        'video_url',
    ]


admin.site.register(Attachment_Services, AttachmentServicesAdmin)
