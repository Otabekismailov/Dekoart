from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from apps.core.models import *
from apps.core.serializers import *
from apps.dictionary.views import StandardResultsSetPagination
from rest_framework.parsers import MultiPartParser, FormParser


class SlideListAPIView(APIView):
    pagination_class = StandardResultsSetPagination
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        language = self.request.query_params.get('language')
        if language == LANGUAGE.RU:
            language = LANGUAGE.RU
        else:
            language = LANGUAGE.UZ
        queryset = Slide.objects.all()
        if queryset:
            serializer = SlideSerializer(
                queryset, context={'language': language}, many=True)
            return Response(serializer.data)
        else:
            return Response([])


class ShortQAListAPIView(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request, format=None):
        language = self.request.query_params.get('language')
        if language == LANGUAGE.RU:
            language = LANGUAGE.RU
        else:
            language = LANGUAGE.UZ
        queryset = ShortQA.objects.all()
        if queryset:
            serializer = ShortQASerializer(
                queryset, context={'language': language}, many=True)
            return Response(serializer.data)
        else:
            return Response([])


class SocialLinkListAPIView(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request, format=None):
        language = self.request.query_params.get('language')
        if language == LANGUAGE.RU:
            language = LANGUAGE.RU
        else:
            language = LANGUAGE.UZ
        queryset = SocialLink.objects.all()
        if queryset:
            serializer = SocialLinkSerializer(
                queryset, context={'language': language}, many=True)
            return Response(serializer.data)
        else:
            return Response([])


class UsefulLinkListAPIView(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request, format=None):
        language = self.request.query_params.get('language')
        if language == LANGUAGE.RU:
            language = LANGUAGE.RU
        else:
            language = LANGUAGE.UZ
        queryset = UsefulLink.objects.all()
        if queryset:
            serializer = UsefulLinkSerializer(
                queryset, context={'language': language}, many=True)
            return Response(serializer.data)
        else:
            return Response([])


class ContactListAPIView(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request, format=None):
        language = self.request.query_params.get('language')
        if language == LANGUAGE.RU:
            language = LANGUAGE.RU
        else:
            language = LANGUAGE.UZ
        queryset = Contact.objects.all()
        if queryset:
            serializer = ContactSerializer(
                queryset, context={'language': language}, many=True)
            return Response(serializer.data)
        else:
            return Response([])


class RepairTypeListAPIView(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request, format=None):
        language = self.request.query_params.get('language')
        if language == LANGUAGE.RU:
            language = LANGUAGE.RU
        else:
            language = LANGUAGE.UZ
        queryset = RepairType.objects.all()
        if queryset:
            serializer = RepairTypeSerializer(
                queryset, context={'language': language}, many=True)
            return Response(serializer.data)
        else:
            return Response([])


class AboutUsListAPIView(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request, format=None):
        language = self.request.query_params.get('language')
        if language == LANGUAGE.RU:
            language = LANGUAGE.RU
        else:
            language = LANGUAGE.UZ
        queryset = AboutUs.objects.all()
        if queryset:
            serializer = AboutUsSerializer(
                queryset, context={'language': language}, many=True)
            return Response(serializer.data)
        else:
            return Response([])


class InfoListAPIView(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        language = self.request.query_params.get('language')
        if language == LANGUAGE.RU:
            language = LANGUAGE.RU
        else:
            language = LANGUAGE.UZ
        queryset = Info.objects.all()
        if queryset:
            serializer = InfoSerializer(
                queryset, context={'language': language}, many=True)
            return Response(serializer.data)
        else:
            return Response([])
