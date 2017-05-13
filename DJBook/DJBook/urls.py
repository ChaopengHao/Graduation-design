"""DJBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from web import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^home/', views.home),
    url(r'^index_change/', views.index_change),
    url(r'^bookinfo/(?P<pk>\d+)/$', views.book_info),
    url(r'^login/', views.user_login),
    url(r'^logout/', views.user_logout),
    url(r'^register/', views.register),
    url(r'^order/', views.order),
    url(r'^orderinfo/', views.order_info),
    url(r'^cart/', views.cart),
    url(r'^userinfo/', views.user_info),
]
