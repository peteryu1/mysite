from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from .views import here, math
from restaurants.views import menu


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^here/$', here),
    url(r'^(\d{1,2})/math/(\d{1,2})/$', math),
    url(r'^menu/$', menu),
)
