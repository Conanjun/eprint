from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'login','backend.views.admin_login',name='admin_login'),
)
