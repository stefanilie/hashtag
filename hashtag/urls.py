from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hashtag.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'search.views.home', name='home')
    url(r'^search/', 'search.views.search', name='search'),
    url(r'^admin/', include(admin.site.urls)),
)
