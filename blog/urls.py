from django.conf.urls import patterns, include, url

from django.contrib import admin
from blog import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'', views.index),
)
