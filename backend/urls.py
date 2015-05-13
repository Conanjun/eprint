from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url(r'^$','backend.views.admin_index', name='admin_index_default'),
                       url(r'^login', 'backend.views.admin_login', name='admin_login'),
                       url(r'^index', 'backend.views.admin_index', name='admin_index'),
                       url(r'^print_orders_list', 'backend.views.admin_print_orders', name='admin_print_orders'),
                       url(r'^trial_orders_list', 'backend.views.admin_trial_orders', name='admin_trial_orders'),
                       url(r'^download_files/*','backend.views.download_files',name='download_files'),
)

