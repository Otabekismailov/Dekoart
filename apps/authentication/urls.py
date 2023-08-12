from django.urls import path
from apps.authentication.views import RegisterUser, LoginView, Logout

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),

]
