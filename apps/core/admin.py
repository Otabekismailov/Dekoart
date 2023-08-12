from django.contrib import admin
from apps.core.models import *

from modeltranslation.admin import TranslationAdmin


class SlideAdmin(TranslationAdmin):
    list_display = [
        'id',
        'title',
        'description',
        'photo_url',
    ]


admin.site.register(Slide, SlideAdmin)


class ShortQAAdmin(TranslationAdmin):
    list_display = [
        'id',
        'title',
        'description',
        'photo_url',
    ]


admin.site.register(ShortQA, ShortQAAdmin)


class SocialLinkAdmin(TranslationAdmin):
    list_display = [
        'id',
        'name',
        'icon',
        'link',
    ]


admin.site.register(SocialLink, SocialLinkAdmin)


class UsefulLinkAdmin(TranslationAdmin):
    list_display = [
        'id',
        'name',
        'link',
    ]


admin.site.register(UsefulLink, UsefulLinkAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'type',
        'icon',
        'data',
    ]


admin.site.register(Contact, ContactAdmin)


class RepairTypeAdmin(TranslationAdmin):
    list_display = [
        'id',
        'name',
        'photo_url',
    ]


admin.site.register(RepairType, RepairTypeAdmin)


class AboutUsAdmin(TranslationAdmin):
    list_display = [
        'id',
        'title',
        'photo_url',
    ]


admin.site.register(AboutUs, AboutUsAdmin)


class Attachment_AboutUsAdmin(TranslationAdmin):
    list_display = [
        'id',
        'about_us',
        'name',
        'photo_url',
    ]


admin.site.register(Attachment_AboutUs, Attachment_AboutUsAdmin)


class InfoAdmin(TranslationAdmin):
    list_display = [
        'id',
        'title',
        'photo_url',
    ]


admin.site.register(Info, InfoAdmin)


class Attachment_InfoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'info',
        'icon',
    ]


admin.site.register(Attachment_Info, Attachment_InfoAdmin)
