from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'eprint.views.home', name='home'),
                       url(r'^register$', 'eprint.views.register', name='register'),
                       url(r'^api/register$', 'eprint.views.api_register', name='api_register'),
                       url(r'^login$', 'eprint.views.user_login', name='user_login'),
                       url(r'^contact$', 'eprint.views.contact', name='contact'),

                       url(r'^dashboard$', include('dashboard.urls')),

                       url(r'^havetry$', 'order.views.have_try', name='have_try'),

                       url(r'^trial_order$', 'order.views.trial_order', name='trial_order'),
                       url(r'print_order$', 'order.views.print_order', name='print_order'),
                       #url(r'backend','backend.views.admin_login',name='admin_login'),
                       url(r'^backend/',include('backend.urls')),

                       # url(r'^eprint/', include('eprint.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
)

