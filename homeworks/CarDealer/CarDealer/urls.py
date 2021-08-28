"""CarDealer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('cars/', include('cars.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.cars.views import *
from apps.dealers.views import *
from apps.orders.views import *
from apps.newsletter.views import *
from apps.accounts.views import *
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexTemplateView.as_view(), name='index'),
    path('cars/', CarView.as_view(), name='car_list'),
    path('cars/<int:pk>', CarDetailView.as_view(), name='car_detail'),
    path('api/cars/json', serializer_cars),
    path('dealers/', DealerView.as_view(), name='dealer_list'),
    path('dealers/<slug:slug>', DealerDetailView.as_view(), name='dealer_detail'),
    path('api/dealers/json', serializer_dealers),
    path('orders/', OrderView.as_view(), name='order_list'),
    path('orders/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('api/orders/json', serializer_order),
    path('newsletter/', NewsLettersView.as_view(), name='newsletter'),
    path('success/', SuccessTemplateView.as_view(), name='success'),
    # path('api-token-auth/', obtain_auth_token),
    # path('demo/', DemoView.as_view(), name='demo'),
    path('signup/', signup, name='signup'),
    path('login/', logIn, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    # REST FRAMEWORK URLS
    path('api/', include('apps.accounts.urls')),
    path('api-auth/', include('rest_framework.urls'))

]
