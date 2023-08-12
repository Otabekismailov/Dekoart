from modeltranslation.translator import TranslationOptions, register

from .models import Info, Attachment_Info, Attachment_AboutUs, AboutUs, RepairType, UsefulLink, SocialLink, ShortQA, \
    Slide


@register(Info)
class InfoTranslationOptions(TranslationOptions):
    fields = ("title", "description",)
    required_languages = ("ru", "uz")


@register(Attachment_AboutUs)
class AttachmentAboutUsTranslationOptions(TranslationOptions):
    fields = ("name",)
    required_languages = ("ru", "uz")


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ("title", "description",)
    required_languages = ("ru", "uz")


@register(RepairType)
class RepairTypeTranslationOptions(TranslationOptions):
    fields = ("name", "description",)
    required_languages = ("ru", "uz")


@register(UsefulLink)
class RepairTypeTranslationOptions(TranslationOptions):
    fields = ("name",)
    required_languages = ("ru", "uz",)


@register(SocialLink)
class RepairTypeTranslationOptions(TranslationOptions):
    fields = ("name",)
    required_languages = ("ru", "uz",)


@register(ShortQA)
class RepairTypeTranslationOptions(TranslationOptions):
    fields = ("title", "description",)
    required_languages = ("ru", "uz")


@register(Slide)
class RepairTypeTranslationOptions(TranslationOptions):
    fields = ("title", "description",)
    required_languages = ("ru", "uz")
