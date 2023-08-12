from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from apps.core.models import LANGUAGE
from apps.dictionary.models import Country
from apps.dictionary.serializers import *


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'limit'
    max_page_size = 1000


class ShopListAPIView(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request, format=None):
        language = self.request.query_params.get('language')
        if language ==LANGUAGE.RU:
            language = LANGUAGE.RU
        else:
            language = LANGUAGE.UZ
        queryset = Country.objects.all()
        if queryset:
            serializer = MallsListSerializer(
                queryset, context={'language': language}, many=True)
            return Response(serializer.data)
        else:
            return Response([])
