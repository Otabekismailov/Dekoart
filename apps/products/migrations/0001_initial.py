# Generated by Django 4.2.4 on 2023-08-11 10:16

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=511)),
                ('name_uz', models.CharField(max_length=511, null=True)),
                ('name_ru', models.CharField(max_length=511, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, limit_choices_to={'is_active': True, 'parent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.category', verbose_name='Parent Category')),
            ],
        ),
        migrations.CreateModel(
            name='Masters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=511, null=True)),
                ('name_uz', models.CharField(blank=True, max_length=511, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=511, null=True)),
                ('views_count', models.PositiveIntegerField(default=0)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('description_uz', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
            options={
                'ordering': ['created_at', 'updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=511, null=True)),
                ('title_uz', models.CharField(blank=True, max_length=511, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=511, null=True)),
                ('views_count', models.PositiveIntegerField(default=0)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('description_uz', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
            options={
                'ordering': ['created_at', 'updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServicesType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=511)),
                ('name_uz', models.CharField(max_length=511, null=True)),
                ('name_ru', models.CharField(max_length=511, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=511, null=True)),
                ('title_uz', models.CharField(blank=True, max_length=511, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=511, null=True)),
                ('views_count', models.PositiveIntegerField(default=0)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name="Ma'lumot")),
                ('description_uz', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name="Ma'lumot")),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name="Ma'lumot")),
                ('photo_url', models.URLField(blank=True, null=True)),
                ('video_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'ordering': ['created_at', 'updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=511, null=True, verbose_name='Nomi')),
                ('name_uz', models.CharField(blank=True, max_length=511, null=True, verbose_name='Nomi')),
                ('name_ru', models.CharField(blank=True, max_length=511, null=True, verbose_name='Nomi')),
                ('views_count', models.PositiveIntegerField(default=0)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('description_uz', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services_type_to_services', to='products.servicestype')),
            ],
            options={
                'ordering': ['created_at', 'updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=511, null=True, verbose_name='Nomi')),
                ('name_uz', models.CharField(blank=True, max_length=511, null=True, verbose_name='Nomi')),
                ('name_ru', models.CharField(blank=True, max_length=511, null=True, verbose_name='Nomi')),
                ('title', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('title_uz', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('title_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('views_count', models.PositiveIntegerField(default=0)),
                ('coefficient', models.PositiveIntegerField(blank=True, null=True)),
                ('photo_url', models.URLField(blank=True, null=True)),
                ('video_url', models.URLField(blank=True, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('description_uz', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_to_product', to='products.category')),
            ],
            options={
                'ordering': ['created_at', 'updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FigureOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('photo_url', models.URLField(blank=True, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='figure_out_to_product', to='products.product')),
            ],
            options={
                'ordering': ['created_at', 'updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ColorCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=511, null=True)),
                ('name_uz', models.CharField(blank=True, max_length=511, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=511, null=True)),
                ('photo_url', models.URLField(blank=True, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='color_catalog_to_product', to='products.product')),
            ],
            options={
                'ordering': ['created_at', 'updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attachment_Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.URLField(blank=True, null=True)),
                ('video_url', models.URLField(blank=True, null=True)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services_to_attachment', to='products.services')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment_News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=31, null=True)),
                ('title_uz', models.CharField(blank=True, max_length=31, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=31, null=True)),
                ('photo_url', models.URLField(blank=True, null=True)),
                ('video_url', models.URLField(blank=True, null=True)),
                ('news', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news_to_attachment', to='products.news')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment_Masters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.URLField(blank=True, null=True)),
                ('video_url', models.URLField(blank=True, null=True)),
                ('master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='masters_to_attachment', to='products.masters')),
            ],
        ),
    ]