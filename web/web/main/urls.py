from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^browserid/', include('django_browserid.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login-failed/$', views.login_failed, name='login-failed'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'},
        name='logout'),
)
