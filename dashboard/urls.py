from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dashboard.views.dashboard', name='dashboard'),
    url(r'^update_profile$', 'dashboard.views.update_profile', name='update_profile'),
)
