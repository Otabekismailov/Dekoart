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
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('name_uz', models.CharField(blank=True, max_length=255, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('name_uz', models.CharField(blank=True, max_length=255, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('information_uz', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('information_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('working_hours', models.CharField(blank=True, max_length=63, null=True)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='district_to_shops', to='dictionary.district')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('name_uz', models.CharField(blank=True, max_length=255, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='region_to_country', to='dictionary.country')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='district_to_region', to='dictionary.region'),
        ),
    ]
