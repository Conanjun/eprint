from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url(r'^$', 'backend.views.backend_index', name='backend_index_default'),
                       url(r'^login$', 'backend.views.backend_login', name='backend_login'),
                       url(r'^index$', 'backend.views.backend_index', name='backend_index'),
                       url(r'^print_orders_list$', 'backend.views.backend_print_orders', name='backend_print_orders'),
                       url(r'^trial_orders_list$', 'backend.views.backend_trial_orders', name='backend_trial_orders'),
                       url(r'^download_files/(?P<order_type>\w+)/(?P<order_id>\d+)/$', 'backend.views.download_files', name='backend_download'),
                       url(r'^change_order_status/(?P<order_id>\d+)/(?P<new_status>\d+)/$', 'backend.views.change_order_status',name='change_order_status'),
                       )

