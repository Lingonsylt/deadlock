from django.conf.urls import patterns, include, url

from django.contrib import admin
from blog import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'p(?P<slug>[a-z0-9-]+)/', views.post, name="post"),
    url(r'', views.blog, name="blog"),
)
