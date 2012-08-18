from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'web.main.views.home', name='home'),
    url(r'^login-failed/$', 'web.main.views.login_failed',
        name='login-failed'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^browserid/', include('django_browserid.urls')),
    url(r'^sign-out/$', 'django.contrib.auth.views.logout', {'next_page': '/'},
        name='sign_out'),
)
