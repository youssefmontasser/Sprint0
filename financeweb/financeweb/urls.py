from django.conf.urls import patterns, include, url
from django.contrib import admin
from financeweb.views import home, abc, home2

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'financeweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^homepage2$', home2, name='home2'),
	url(r'^signup$', abc, name='abc'),
)
