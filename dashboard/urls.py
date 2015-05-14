from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'dashboard.views.dashboard', name='dashboard'),
    url(r'^update_profile$', 'dashboard.views.update_profile', name='update_profile'),
)
