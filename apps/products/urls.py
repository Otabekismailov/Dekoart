from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from apps.products.views import *

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('category-list/', CategoryListAPIView.as_view(), name='category-list'),
    path('productlist/', ProductsForAdminListAPIView.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('videos/', VideoListAPIView.as_view(), name='videos'),
    path('videos/<int:pk>/', VideoDetail.as_view()),
    path('news/', NewsListAPIView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetail.as_view()),
    path('masters/', MastersListAPIView.as_view(), name='masters'),
    path('masters/<int:pk>/', MastersDetail.as_view()),
    path('servicestype/', ServicesTypeListAPIView.as_view(), name='servicestype'),
    path('services/<int:pk>/', ServicesDetail.as_view()),
]

app_name = 'products'
