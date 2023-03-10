"""dsaDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path
from market.views import show_cars, audi_purchase
from views_weather import show_weather
from views_name import name


def hello_world(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),
    path('weather/', show_weather),
    path('audi/', show_cars),
    path('buy_car/<int:id_>', audi_purchase),
    path('name/', name),
]
