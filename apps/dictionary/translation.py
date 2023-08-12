from modeltranslation.translator import TranslationOptions, register

from .models import Country, Region, District, Shops


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ("name",)
    required_languages = ("ru", "uz")


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ("name",)
    required_languages = ("ru", "uz")


@register(District)
class DistrictTranslationOptions(TranslationOptions):
    fields = ("name",)
    required_languages = ("ru", "uz")


@register(Shops)
class ShopsTranslationOptions(TranslationOptions):
    fields = ("information",)
    required_languages = ("ru", "uz")