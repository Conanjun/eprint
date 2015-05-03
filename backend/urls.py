from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
   # url(r'^$''backend.views.admin_login',name='admin_login_default'),
    url(r'^login','backend.views.admin_login',name='admin_login'),
    url(r'^api/login','backend.views.api_admin_login',name='api_admin_login'),
)
