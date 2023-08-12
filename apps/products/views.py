from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from apps.core.models import LANGUAGE
from apps.dictionary.views import StandardResultsSetPagination
from apps.products.serializers import *
from drf_yasg.utils import swagger_auto_schema


class CategoryListAPIView(APIView):
    pagination_class = StandardResultsSetPagination


    def get(self, request):
        language = self.request.query_params.get('language')
        if language == LANGUAGE.RU:
            language = LANGUAGE.RU
        else:
            language = LANGUAGE.UZ
        queryset = Category.objects.all()
        if queryset:
            serializer = ProductsListSerializer(
                queryset, context={'language': language}, many=True)
            return Response(serializer.data)
        else:
            return Response([])


class ProductsForAdminListAPIView(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        language = self.request.query_params.get('language')
        if language == LANGUAGE.RU:
            language = LANGUAGE.RU
        else:
            language = LANGUAGE.UZ
        queryset = Product.objects.all()
        if queryset:
            serializer = ProductForListSerializer(
                queryset, context={'language': language}, many=True)
            return Response(serializer.data)
        else:
            return Response([])


class ProductDetail(APIView):
    pagination_class = StandardResultsSetPagination

    def get_object(self, pk):
        try:
            product = get_object_or_404(Product, id=pk)
            return product
        except ValueError:
            raise Http404

    def get(self, request, pk):
        language = self.request.query_params.get('language')
        if language == LANGUAGE.RU:
            language = LANGUAGE.RU
        else:
            language = LANGUAGE.UZ
        queryset = self.get_object(pk)
        queryset.views_count += 1
        queryset.save()
        serializer = ProductRetrieveSerializer(
            queryset, context={'language': language}, many=False)
        return Response(serializer.data)


class VideoListAPIView(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        language = self.request.query_params.get('language')
        if language == LANGUAGE.RU:
            language = LANGUAGE.RU
        else:
            language = LANGUAGE.UZ
        queryset = Videos.objects.all()
        if queryset:
            serializer = VideosListSerializer(
                queryset, context={'language': language}, many=True)
            return Response(serializer.data)
        else:
            return Response([])


class VideoDetail(APIView):
    pagination_class = StandardResultsSetPagination

    def get_object(self, pk):
        try:
            video = get_object_or_404(Videos, id=pk)
            return video
        except ValueError:
            raise Http404

    def get(self, request, pk):
        language = self.request.query_params.get('language')
        if language == LANGUAGE.RU:
            language = LANGUAGE.RU
        else:
            language = LANGUAGE.UZ
        queryset = self.get_object(pk)
        queryset.views_count += 1
        queryset.save()
        serializer = VideoRetrieveSerializer(
            queryset, context={'language': language}, many=False)
        return Response(serializer.data)


class NewsListAPIView(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        language = self.request.query_params.get('language')
        if language == LANGUAGE.RU:
            language = LANGUAGE.RU
        else:
            language = LANGUAGE.UZ
        queryset = News.objects.all()
        if queryset:
            serializer = NewsListSerializer(
                queryset, context={'language': language}, many=True)
            return Response(serializer.data)
        else:
            return Response([])


class NewsDetail(APIView):
    pagination_class = StandardResultsSetPagination

    def get_object(self, pk):
        try:
            news = get_object_or_404(News, id=pk)
            return news
        except ValueError:
            raise Http404

    def get(self, request, pk):
        language = self.request.query_params.get('language')
        if language == LANGUAGE.RU:
            language = LANGUAGE.RU
        else:
            language = LANGUAGE.UZ
        queryset = self.get_object(pk)
        queryset.views_count += 1
        queryset.save()
        serializer = NewsRetrieveSerializer(
            queryset, context={'language': language}, many=False)
        return Response(serializer.data)


class MastersListAPIView(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        language = self.request.query_params.get('language')
        if language == LANGUAGE.RU:
            language = LANGUAGE.RU
        else:
            language = LANGUAGE.UZ
        queryset = Masters.objects.all()
        if queryset:
            serializer = MastersListSerializer(
                queryset, context={'language': language}, many=True)
            return Response(serializer.data)
        else:
            return Response([])


class MastersDetail(APIView):
    pagination_class = StandardResultsSetPagination

    def get_object(self, pk):
        try:
            master = get_object_or_404(Masters, id=pk)
            return master
        except ValueError:
            raise Http404

    def get(self, request, pk):
        language = self.request.query_params.get('language')
        if language == LANGUAGE.RU:
            language = LANGUAGE.RU
        else:
            language = LANGUAGE.UZ
        queryset = self.get_object(pk)
        queryset.views_count += 1
        queryset.save()
        serializer = MasterRetrieveSerializer(
            queryset, context={'language': language}, many=False)
        return Response(serializer.data)


class ServicesDetail(APIView):
    pagination_class = StandardResultsSetPagination

    def get_object(self, pk):
        try:
            service = get_object_or_404(ServicesType, id=pk)
            return service
        except ValueError:
            raise Http404

    def get(self, request, pk):
        language = self.request.query_params.get('language')
        if language == LANGUAGE.RU:
            language = LANGUAGE.RU
        else:
            language = LANGUAGE.UZ
        queryset = self.get_object(pk)
        services = Services.objects.get(type=queryset)
        services.views_count += 1
        services.save()
        serializer = ServicesTypeRetrieveSerializer(
            queryset, context={'language': language}, many=False)
        return Response(serializer.data)


class ServicesTypeListAPIView(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        language = self.request.query_params.get('language')
        if language == LANGUAGE.RU:
            language = LANGUAGE.RU
        else:
            language = LANGUAGE.UZ
        queryset = ServicesType.objects.all()
        if queryset:
            serializer = ServicesTypeListSerializer(
                queryset, context={'language': language}, many=True)
            return Response(serializer.data)
        else:
            return Response([])
