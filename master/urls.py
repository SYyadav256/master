"""
URL configuration for master project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from master import views
from django.http import HttpResponse
from django.shortcuts import render

urlpatterns = [
    path('adminpanel/', admin.site.urls),
    path('home/',views.home),
    path('course/<courseid>',views.coursedetails), 
    path('',views.homepage),
    path('basic/',views.basic),
    path('forloop/',views.forloop),
    path('ifelse/',views.ifelse),
    path('home/',views.home),
    path('about/',views.about),
    path('services/',views.services),
    path('contact/',views.contact),
    path("index1/",views.index1),
    path("header/",views.header),
    path("footer/",views.footer),
    path("base/",views.base),
    path("navbar/",views.navbar),
    path("l17/",views.l17),
    path("l18/",views.l18),
    path("l19/",views.l19),
    path("l20/",views.l20),
    path("l22/",views.l22),
    path("l23/",views.l23),
    path("l24/",views.l24),

]
