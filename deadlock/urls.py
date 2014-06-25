from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.http import Http404
import blog

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^$', blog.views.about, name="about"),
)