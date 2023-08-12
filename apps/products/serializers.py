from rest_framework import serializers
from django.db.models import Q
from apps.core.models import LANGUAGE
from apps.products.models import *


class ServicesTypeListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = ServicesType
        fields = ['id', 'name']
    
    def get_name(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.name_ru is not None:
                return obj.name_ru
            else:
                return None
        else:
            if obj.name_uz is not None:
                return obj.name_uz
            else:
                return None


class ProductForListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'views_count', 'photo_url', 'title']
    
    def get_name(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.name_ru is not None:
                return obj.name_ru
            else:
                return None
        else:
            if obj.name_uz is not None:
                return obj.name_uz
            else:
                return None
    
    def get_title(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.title_ru is not None:
                return obj.title_ru
            else:
                return None
        else:
            if obj.title_uz is not None:
                return obj.title_uz
            else:
                return None


class ProductsListSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'product']
    
    def get_product(self, obj):
        language = self.context['language']
        product = Product.objects.filter(
            Q(category=obj)
        )
        if product:
            serializer = ProductForListSerializer(
                product, context={'language': language}, many=True)
            return serializer.data
        else:
            return None

    def get_name(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.name_ru is not None:
                return obj.name_ru
            else:
                return None
        else:
            if obj.name_uz is not None:
                return obj.name_uz
            else:
                return None


class FigureOutSerializer(serializers.ModelSerializer):

    class Meta:
        model = FigureOut
        fields = ['id', 'photo_url']


class ColorCatalogSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = ColorCatalog
        fields = ['id', 'name', 'photo_url']
    
    def get_name(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.name_ru is not None:
                return obj.name_ru
            else:
                return None
        else:
            if obj.name_uz is not None:
                return obj.name_uz
            else:
                return None


class ProductRetrieveSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    figure_out = serializers.SerializerMethodField()
    color_catalog = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'coefficient', 'views_count',
                  'photo_url', 'video_url', 'title', 'description', 
                  'figure_out', 'color_catalog']
    
    def get_category(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            return obj.category.name_ru
        else:
            return obj.category.name_uz

    def get_name(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.name_ru is not None:
                return obj.name_ru
            else:
                return None
        else:
            if obj.name_uz is not None:
                return obj.name_uz
            else:
                return None
    
    def get_title(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.title_ru is not None:
                return obj.title_ru
            else:
                return None
        else:
            if obj.title_uz is not None:
                return obj.title_uz
            else:
                return None
    
    def get_description(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.description_ru is not None:
                return obj.description_ru
            else:
                return None
        else:
            if obj.description_uz is not None:
                return obj.description_uz
            else:
                return None
    
    def get_figure_out(self, obj):
        language = self.context['language']
        figureOut = FigureOut.objects.filter(
            Q(product=obj)
        )
        if figureOut:
            serializer = FigureOutSerializer(
                figureOut, context={'language': language}, many=True)
            return serializer.data
        else:
            return None
    
    def get_color_catalog(self, obj):
        language = self.context['language']
        colorCatalog = ColorCatalog.objects.filter(
            Q(product=obj)
        )
        if colorCatalog:
            serializer = ColorCatalogSerializer(
                colorCatalog, context={'language': language}, many=True)
            return serializer.data
        else:
            return None


class VideosListSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = Videos
        fields = ['id', 'title', 'views_count', 'photo_url']

    def get_title(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.title_ru is not None:
                return obj.title_ru
            else:
                return None
        else:
            if obj.title_uz is not None:
                return obj.title_uz
            else:
                return None


class VideoRetrieveSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Videos
        fields = ['id', 'title', 'description', 'views_count', 'photo_url', 'video_url']

    def get_title(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.title_ru is not None:
                return obj.title_ru
            else:
                return None
        else:
            if obj.title_uz is not None:
                return obj.title_uz
            else:
                return None
    
    def get_description(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.description_ru is not None:
                return obj.description_ru
            else:
                return None
        else:
            if obj.description_uz is not None:
                return obj.description_uz
            else:
                return None


class NewsListSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'photo', 'views_count']
    
    def get_photo(self, obj):
        news = Attachment_News.objects.filter(
            Q(news=obj)
        ).first()
        if news:
            return news.photo_url
        else:
            return None

    def get_description(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.description_ru is not None:
                return f"{obj.description_ru[:50]}..."
            else:
                return None
        else:
            if obj.description_uz is not None:
                return f"{obj.description_uz[:50]}..."
            else:
                return None

    def get_title(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.title_ru is not None:
                return obj.title_ru
            else:
                return None
        else:
            if obj.title_uz is not None:
                return obj.title_uz
            else:
                return None





class Attachment_NewsSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = Attachment_News
        fields = ['id', 'title', 'photo_url', 'video_url']
    
    def get_title(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.title_ru is not None:
                return obj.title_ru
            else:
                return None
        else:
            if obj.title_uz is not None:
                return obj.title_uz
            else:
                return None


class NewsRetrieveSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    attachment = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'views_count', 'description', 
                  'attachment']

    def get_title(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.title_ru is not None:
                return obj.title_ru
            else:
                return None
        else:
            if obj.title_uz is not None:
                return obj.title_uz
            else:
                return None
    
    def get_description(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.description_ru is not None:
                return obj.description_ru
            else:
                return None
        else:
            if obj.description_uz is not None:
                return obj.description_uz
            else:
                return None
    
    def get_attachment(self, obj):
        language = self.context['language']
        attachment_News = Attachment_News.objects.filter(
            Q(news=obj)
        )
        if attachment_News:
            serializer = Attachment_NewsSerializer(
                attachment_News, context={'language': language}, many=True)
            return serializer.data
        else:
            return None


class MastersListSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Masters
        fields = ['id', 'name', 'description', 'photo', 'views_count']
    
    def get_photo(self, obj):
        attachment = Attachment_Masters.objects.filter(
            Q(master=obj)
        ).first()
        if attachment:
            return attachment.photo_url
        else:
            return None

    def get_description(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.description_ru is not None:
                return f"{obj.description_ru[:50]}..."
            else:
                return None
        else:
            if obj.description_uz is not None:
                return f"{obj.description_uz[:50]}..."
            else:
                return None

    def get_name(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.name_ru is not None:
                return obj.name_ru
            else:
                return None
        else:
            if obj.name_uz is not None:
                return obj.name_uz
            else:
                return None



class Attachment_MastersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attachment_Masters
        fields = ['id', 'photo_url', 'video_url']


class MasterRetrieveSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    attachment = serializers.SerializerMethodField()

    class Meta:
        model = Masters
        fields = ['id', 'name', 'views_count', 'description', 
                  'attachment']

    def get_name(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.name_ru is not None:
                return obj.name_ru
            else:
                return None
        else:
            if obj.name_uz is not None:
                return obj.name_uz
            else:
                return None
    
    def get_description(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.description_ru is not None:
                return obj.description_ru
            else:
                return None
        else:
            if obj.description_uz is not None:
                return obj.description_uz
            else:
                return None
    
    def get_attachment(self, obj):
        language = self.context['language']
        attachment_masters = Attachment_Masters.objects.filter(
            Q(master=obj)
        )
        if attachment_masters:
            serializer = Attachment_MastersSerializer(
                attachment_masters, many=True)
            return serializer.data
        else:
            return None


class Attachment_ServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attachment_Services
        fields = ['id', 'photo_url', 'video_url']


class RetrieveSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    attachment = serializers.SerializerMethodField()

    class Meta:
        model = Services
        fields = ['id', 'name', 'views_count', 'description', 
                  'attachment']

    def get_name(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.name_ru is not None:
                return obj.name_ru
            else:
                return None
        else:
            if obj.name_uz is not None:
                return obj.name_uz
            else:
                return None
    
    def get_description(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.description_ru is not None:
                return obj.description_ru
            else:
                return None
        else:
            if obj.description_uz is not None:
                return obj.description_uz
            else:
                return None
    
    def get_attachment(self, obj):
        language = self.context['language']
        attachment = Attachment_Services.objects.filter(
            Q(service=obj)
        )
        if attachment:
            serializer = Attachment_ServicesSerializer(
                attachment, many=True)
            return serializer.data
        else:
            return None


class ServicesTypeRetrieveSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    service = serializers.SerializerMethodField()

    class Meta:
        model = ServicesType
        fields = ['id', 'name', 'services']

    def get_name(self, obj):
        language = self.context['language']
        if language == LANGUAGE.RU:
            if obj.name_ru is not None:
                return obj.name_ru
            else:
                return None
        else:
            if obj.name_uz is not None:
                return obj.name_uz
            else:
                return None
    
    def get_services(self, obj):
        language = self.context['language']
        services = Services.objects.filter(
            Q(type=obj)
        )
        if services:
            serializer = Attachment_MastersSerializer(
                services, context={'language': language}, many=False)
            return serializer.data
        else:
            return None