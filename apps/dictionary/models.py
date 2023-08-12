from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from apps.core.models import LANGUAGE


class Country(models.Model):
    name = models.CharField(
        max_length=255, null=True, blank=True
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f'{self.name}'


class Region(models.Model):
    name = models.CharField(
        max_length=255, null=True, blank=True
    )

    country = models.ForeignKey(
        Country,
        null=True,
        on_delete=models.SET_NULL,
        related_name='region_to_country'
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f'{self.name}'


class District(models.Model):
    name= models.CharField(
        max_length=255, null=True, blank=True
    )

    region = models.ForeignKey(
        Region,
        null=True,
        on_delete=models.SET_NULL,
        related_name='district_to_region'
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f'{self.name}'


class Shops(models.Model):
    district = models.ForeignKey(
        District,
        on_delete=models.SET_NULL,
        null=True,
        related_name='district_to_shops'
    )
    information = RichTextUploadingField(null=True, blank=True)
    phone = models.CharField(
        max_length=30, null=True, blank=True, unique=True)
    working_hours = models.CharField(
        max_length=63,
        null=True, blank=True
    )

    def __str__(self):
        return f'{self.district} - {self.information}'
