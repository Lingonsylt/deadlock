from bootlog.views import BSearchView
from django.conf.urls import patterns, include, url

from django.contrib import admin
from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet
from haystack.views import search_view_factory

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('bootlog.urls')),
)
