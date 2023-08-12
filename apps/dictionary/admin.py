from django.contrib import admin

from apps.dictionary.models import *
from modeltranslation.admin import TranslationAdmin


class CountryAdmin(TranslationAdmin):
    list_display = [
        'id',
        'name',

    ]


admin.site.register(Country, CountryAdmin)


class RegionAdmin(TranslationAdmin):
    list_display = [
        'id',
        'country',
        'name',

    ]


admin.site.register(Region, RegionAdmin)


class DistrictAdmin(TranslationAdmin):
    list_display = [
        'id',
        'region',
        'name',

    ]


admin.site.register(District, DistrictAdmin)


class ShopsAdmin(TranslationAdmin):
    list_display = [
        'id',
        'district',
        'information',
        'phone',
        'working_hours',
    ]


admin.site.register(Shops, ShopsAdmin)
