from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'eprint.views.home', name='home'),
                       url(r'^register$', 'eprint.views.register', name='register'),
                       url(r'^login$', 'eprint.views.user_login', name='user_login'),
                       url(r'^contact$', 'eprint.views.contact', name='contact'),
                       url(r'^logout$', 'eprint.views.user_logout', name='user_logout'),

                       url(r'^dashboard/', include('dashboard.urls')),

                       url(r'^trial_order$', 'order.views.trial_order', name='trial_order'),
                       url(r'^print_order$', 'order.views.print_order', name='print_order'),
                       url(r'^backend/', include('backend.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       )

