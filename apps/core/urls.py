from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from apps.core.views import *


router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('slide/', SlideListAPIView.as_view(),  name='slide'),
    path('short_qa/', ShortQAListAPIView.as_view(),  name='short_qa'),
    path('social_link/', SocialLinkListAPIView.as_view(),  name='social_link'),
    path('useful_link/', UsefulLinkListAPIView.as_view(),  name='useful_link'),
    path('contact/', ContactListAPIView.as_view(),  name='contact'),
    path('repair_type/', RepairTypeListAPIView.as_view(),  name='repair_type'),
    path('about_us/', AboutUsListAPIView.as_view(),  name='about_us'),
    path('info/', InfoListAPIView.as_view(),  name='info'),

]

app_name = 'core'