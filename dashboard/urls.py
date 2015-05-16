from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url(r'^$', 'dashboard.views.dashboard', name='dashboard'),
                       url(r'^update_profile$', 'dashboard.views.update_profile', name='update_profile'),
                       url(r'^download_order_file/(?P<order_id>\d+)/$','dashboard.views.download_order_file', name='download_order_file'),
                       )
