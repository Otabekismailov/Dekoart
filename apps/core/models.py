from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class LANGUAGE:
    UZ = 'uz'
    RU = 'ru'


DESCRIPTION = "Description"
ADDRESS = "Address"
PHONE_NUMBER = "Phone number"
EMAIL = "Email"
WEB_SITE = "Web site"

CONTACT_TYPE = (
    (DESCRIPTION, 'Description'),
    (ADDRESS, 'Address'),
    (PHONE_NUMBER, 'Phone number'),
    (EMAIL, 'Email'),
    (WEB_SITE, 'Web site'),
)


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['created_at', 'updated_at']


class Slide(models.Model):
    title = models.CharField(
        null=True, blank=True,
        max_length=511,

    )

    description = RichTextUploadingField(
        null=True, blank=True,

    )
    photo_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class ShortQA(models.Model):
    title = models.CharField(
        max_length=511,
        null=True, blank=True,

    )

    description = RichTextUploadingField(
        null=True, blank=True,

    )
    photo_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class SocialLink(models.Model):
    name = models.CharField(
        max_length=31,
        null=True, blank=True,
    )

    icon = models.CharField(
        max_length=63,
        null=True, blank=True,
        verbose_name="Ikonka klas nomi"
    )
    link = models.URLField(
        null=True, blank=True,
        verbose_name="Manzil"
    )

    def __str__(self):
        return self.name


class UsefulLink(models.Model):
    name = models.CharField(
        max_length=31,
        null=True, blank=True,

    )

    link = models.URLField(
        null=True, blank=True,
        verbose_name="Manzil"
    )

    def __str__(self):
        return self.name


class Contact(models.Model):
    type = models.CharField(
        max_length=127,
        verbose_name="Turi",
        null=True, blank=True,
        choices=CONTACT_TYPE,
    )
    icon = models.CharField(
        max_length=63,
        null=True, blank=True,
        verbose_name="Ikonka klas nomi"
    )
    data = RichTextUploadingField(
        null=True, blank=True,

    )

    def __str__(self):
        return f"contact ID{self.id}: {self.type}"


class RepairType(models.Model):
    name = models.CharField(
        max_length=31,
        null=True, blank=True,
    )

    description = RichTextUploadingField(
        null=True, blank=True,

    )

    photo_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"repairtype ID{self.id}: {self.name}"


class AboutUs(models.Model):
    title = models.CharField(
        max_length=511,
        null=True, blank=True,

    )

    description = RichTextUploadingField(
        null=True, blank=True,

    )

    photo_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"about_us ID{self.id}: {self.title}"


class Attachment_AboutUs(models.Model):
    about_us = models.ForeignKey(
        AboutUs,
        on_delete=models.SET_NULL,
        null=True,
        related_name='about_us_attachment'
    )
    name = models.CharField(
        max_length=31,
        null=True, blank=True,

    )

    photo_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"attachment_about_us ID{self.id}: {self.name}"


class Info(models.Model):
    title = models.CharField(
        max_length=511,
        null=True, blank=True,

    )

    description = RichTextUploadingField(
        null=True, blank=True
    )

    photo_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"about_us ID{self.id}: {self.title}"


class Attachment_Info(models.Model):
    info = models.ForeignKey(
        Info,
        on_delete=models.SET_NULL,
        null=True,
        related_name='info_attachment'
    )
    icon = models.CharField(
        max_length=63,
        null=True, blank=True,
        verbose_name="Ikonka klas nomi"
    )

    def __str__(self):
        return f"attachment_about_us ID{self.id}: {self.icon}"
