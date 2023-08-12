from modeltranslation.translator import TranslationOptions, register

from .models import Category, Product, ColorCatalog, News, Attachment_News, Videos, Masters, ServicesType, Services


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)
    required_languages = ("ru", "uz",)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ("name", "title", "description",)
    required_languages = ("ru", "uz")


@register(ColorCatalog)
class ColorCatalogTranslationOptions(TranslationOptions):
    fields = ("name",)
    required_languages = ("ru", "uz")


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ("title", "description",)
    required_languages = ("ru", "uz")


@register(Attachment_News)
class AttachmentNewsTranslationOptions(TranslationOptions):
    fields = ("title",)
    required_languages = ("ru", "uz")


@register(Videos)
class VideosTranslationOptions(TranslationOptions):
    fields = ("title", "description")
    required_languages = ("ru", "uz")


@register(Masters)
class VideosTranslationOptions(TranslationOptions):
    fields = ("name", "description")
    required_languages = ("ru", "uz")


@register(ServicesType)
class ServicesTypeTranslationOptions(TranslationOptions):
    fields = ("name",)
    required_languages = ("ru", "uz")


@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ("name", "description")
    required_languages = ("ru", "uz")
