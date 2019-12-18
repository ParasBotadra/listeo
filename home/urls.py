from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import home.views as views

urlpatterns = [
url(r'^$', views.Homepage.as_view(), name='homepage'),
url(r'listings', views.Listings.as_view(), name='listings'),
]
