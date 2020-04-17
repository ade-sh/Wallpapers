"""Wallpapers URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('', views.index, name="index"),
    path('page/<int:page>/', views.browsepages, name="browsePage"),
    path('category/<str:categ>/<int:page>/', views.browse_category, name="browse_category"),
    path('category/<str:categ>', views.browse_category, {'page': 1}, name="browse_category"),
    path('wdp/<int:wid>', views.wallpaper_description_page, name="WDPage"),
    path('download/<int:product_id>', views.download_image, name="downloadImage"),
]
