from django.urls import include, path
from .views import *

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='registerapi'),
    path('login/', LoginAPIView.as_view(), name='loginapi'),
    path('logout/', LogoutAPIView.as_view(), name='logoutapi'),
    path('users/', UserAPIView.as_view(), name='userapi'),
]


