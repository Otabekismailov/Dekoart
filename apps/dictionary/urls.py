from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from apps.dictionary.views import ShopListAPIView


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('shops/', ShopListAPIView.as_view(),  name='shops'),

]

app_name = 'dictionary'