from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'eprint.views.home', name='home'),
    url(r'^register$','eprint.views.register', name='register'),
    url(r'^login$','eprint.views.user_login', name='user_login'),
    url(r'^dashboard/',include('dashboard.urls'))
    # url(r'^eprint/', include('eprint.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
