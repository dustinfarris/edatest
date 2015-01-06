from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from people.viewsets import PersonViewSet


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'people', PersonViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'edatest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
)
