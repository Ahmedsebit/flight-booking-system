from django.conf.urls import url
from .views import CustomerAccountApiListView, CustomerAccountApiDetailView, CustomerAccountApiCreateView, CustomerAccountApiUpdateView, CustomerAccountApiDestroyView

urlpatterns = [
    url(r'^$', CustomerAccountApiListView.as_view(), name='customers'),
    url(r'^(?P<pk>\d+)/$', CustomerAccountApiDetailView.as_view(), name='customers_details'),
    url(r'^create/$', CustomerAccountApiCreateView.as_view(), name='customers_create'),
    url(r'^(?P<pk>\d+)/update/$', CustomerAccountApiUpdateView.as_view(), name='customers_update'),
    url(r'^(?P<pk>\d+)/delete/$', CustomerAccountApiDestroyView.as_view(), name='customers_delete')
]
