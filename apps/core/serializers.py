from rest_framework import serializers
from django.db.models import Q

from apps.core.models import *


class SlideSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Slide
        fields = ['id', 'title', 'description', 'photo_url']

    def get_title(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            return obj.title_ru
        else:
            return obj.title_uz

    def get_description(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            return obj.description_ru
        else:
            return obj.description_uz


class ShortQASerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = ShortQA
        fields = ['id', 'title', 'description', 'photo_url']

    def get_title(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            return obj.title_ru
        else:
            return obj.title_uz

    def get_description(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            return obj.description_ru
        else:
            return obj.description_uz


class SocialLinkSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = SocialLink
        fields = ['id', 'name', 'icon', 'link']

    def get_name(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            return obj.name_ru
        else:
            return obj.name_uz


class UsefulLinkSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = UsefulLink
        fields = ['id', 'name', 'link']

    def get_name(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            return obj.name_ru
        else:
            return obj.name_uz


class ContactSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ['id', 'type', 'icon', 'data']

    def get_data(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            return obj.data_ru
        else:
            return obj.data_uz


class RepairTypeSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = RepairType
        fields = ['id', 'name', 'description', 'photo_url']

    def get_name(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            return obj.name_ru
        else:
            return obj.name_uz

    def get_description(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            return obj.description_ru
        else:
            return obj.description_uz


class Attachment_AboutUsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Attachment_AboutUs
        fields = ['id', 'name', 'photo_url']

    def get_name(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            return obj.name_ru
        else:
            return obj.name_uz


class AboutUsSerializer(serializers.ModelSerializer):
    attachment_about_us = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = AboutUs
        fields = ['id', 'title', 'description',
                  'photo_url', 'attachment_about_us']

    def get_attachment_about_us(self, obj):
        attachment = Attachment_AboutUs.objects.filter(
            Q(about_us=obj)
        )
        if attachment:
            language = self.context['language']
            serializer = Attachment_AboutUsSerializer(
                attachment, context={'language': language}, many=True)
            return serializer.data
        else:
            return None

    def get_title(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            return obj.title_ru
        else:
            return obj.title_uz

    def get_description(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            return obj.description_ru
        else:
            return obj.description_uz


class Attachment_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment_Info
        fields = ['id', 'icon']


class InfoSerializer(serializers.ModelSerializer):
    attachment_info = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Info
        fields = ['id', 'title', 'description',
                  'photo_url', 'attachment_info']

    def get_attachment_info(self, obj):
        attachment = Attachment_Info.objects.filter(
            Q(info=obj)
        )
        if attachment:
            serializer = Attachment_InfoSerializer(
                attachment, many=True)
            return serializer.data
        else:
            return None

    def get_title(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            return obj.title_ru
        else:
            return obj.title_uz

    def get_description(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            return obj.description_ru
        else:
            return obj.description_uz
