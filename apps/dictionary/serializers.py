from rest_framework import serializers
from django.db.models import Q
from apps.core.models import LANGUAGE
from apps.dictionary.models import Country, District, Region, Shops


class ShopSerializer(serializers.ModelSerializer):
    information = serializers.SerializerMethodField()

    class Meta:
        model = Shops
        fields = ['id', 'information', 'phone', 'working_hours']

    def get_information(self, obj):
        language = self.context['language']
        if language == LANGUAGE.UZ:
            if obj.information_uz is None:
                return obj.information_uz
            else:
                return None
        else:
            if obj.information_ru is None:
                return obj.information_ru
            else:
                return None


class DistrictSerializer(serializers.ModelSerializer):
    shops = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = District
        fields = ['id', 'name', 'shops']

    def get_shops(self, obj):
        language = self.context['language']
        shops = Shops.objects.filter(
            Q(district=obj)
        )
        if shops:
            serializer = ShopSerializer(
                shops, context={'language': language}, many=True)
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


class RegionSerializer(serializers.ModelSerializer):
    district = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = Region
        fields = ['id', 'name', 'district']

    def get_district(self, obj):
        language = self.context['language']
        district = District.objects.filter(
            Q(region=obj)
        )
        if district:
            serializer = DistrictSerializer(
                district, context={'language': language}, many=True)
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


class MallsListSerializer(serializers.ModelSerializer):
    region = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = ['id', 'name', 'region']

    def get_region(self, obj):
        language = self.context['language']
        region = Region.objects.filter(
            Q(country=obj)
        )
        if region:
            serializer = RegionSerializer(
                region, context={'language': language}, many=True)
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
