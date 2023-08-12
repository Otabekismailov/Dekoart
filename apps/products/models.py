from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from apps.core.models import TimeStampedModel, upload_to


class Category(models.Model):
    name = models.CharField(
        max_length=511,

    )
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Parent Category',
                               limit_choices_to={'is_active': True, 'parent__isnull': True},
                               related_name='children', null=True, blank=True, )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        related_name='category_to_product')
    name = models.CharField(
        max_length=511,
        null=True, blank=True,
        verbose_name="Nomi"
    )

    title = RichTextUploadingField(null=True, blank=True)

    views_count = models.PositiveIntegerField(
        default=0,
    )
    coefficient = models.PositiveIntegerField(null=True, blank=True)
    photo_url = models.URLField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    description = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return f'category ID:{self.category} - {self.name}'


class FigureOut(TimeStampedModel):
    product = models.ForeignKey(
        Product,
        null=True,
        on_delete=models.SET_NULL,
        related_name='figure_out_to_product')
    photo_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'product ID:{self.product}'


class ColorCatalog(TimeStampedModel):
    product = models.ForeignKey(
        Product,
        null=True,
        on_delete=models.SET_NULL,
        related_name='color_catalog_to_product')
    name = models.CharField(
        max_length=511,
        null=True, blank=True,

    )
    photo_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'product ID:{self.product} {self.name}'


class News(TimeStampedModel):
    title = models.CharField(
        null=True, blank=True,
        max_length=511,

    )

    views_count = models.PositiveIntegerField(
        default=0,
    )
    description = RichTextUploadingField(
        null=True, blank=True,

    )

    def __str__(self):
        return f'ID:{self.id} {self.title}'


class Attachment_News(models.Model):
    news = models.ForeignKey(
        News,
        on_delete=models.SET_NULL,
        null=True,
        related_name='news_to_attachment'
    )
    title = models.CharField(
        max_length=31,
        null=True, blank=True,

    )

    photo_url = models.URLField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"news ID{self.news}: {self.title}"


class Videos(TimeStampedModel):
    title = models.CharField(
        null=True, blank=True,
        max_length=511,

    )

    views_count = models.PositiveIntegerField(
        default=0,
    )
    description = RichTextUploadingField(
        null=True, blank=True,
        verbose_name="Ma'lumot"
    )

    photo_url = models.URLField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"ID{self.id}: {self.title}"


class Masters(TimeStampedModel):
    name = models.CharField(
        null=True, blank=True,
        max_length=511,
    )
    views_count = models.PositiveIntegerField(
        default=0,
    )
    description = RichTextUploadingField(
        null=True, blank=True,
    )

    def __str__(self):
        return f'ID:{self.id} {self.name}'


class Attachment_Masters(models.Model):
    master = models.ForeignKey(
        Masters,
        on_delete=models.SET_NULL,
        null=True,
        related_name='masters_to_attachment'
    )
    photo_url = models.URLField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"master: {self.master.name} photo ID:{self.id}"


class ServicesType(models.Model):
    name = models.CharField(
        max_length=511,

    )

    def __str__(self):
        return self.name


class Services(TimeStampedModel):
    type = models.ForeignKey(
        ServicesType,
        null=True,
        on_delete=models.SET_NULL,
        related_name='services_type_to_services')
    name = models.CharField(
        max_length=511,
        null=True, blank=True,
        verbose_name="Nomi"
    )

    views_count = models.PositiveIntegerField(
        default=0,
    )
    description = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return f'type ID:{self.type.name} - {self.name}'


class Attachment_Services(models.Model):
    service = models.ForeignKey(
        Services,
        on_delete=models.SET_NULL,
        null=True,
        related_name='services_to_attachment'
    )
    photo_url = models.URLField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"service: {self.service.name} photo ID:{self.id}"
