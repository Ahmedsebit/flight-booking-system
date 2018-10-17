from django.conf.urls import url
from .views import FlightApiListView,  FlightAPICreateView, FlightApiDetailView, FlightApiDestroyView, FlightApiUpdateView

urlpatterns = [
    url(r'^$', FlightApiListView.as_view(), name='flight'),
    url(r'^create/$', FlightAPICreateView.as_view(), name='flight_create'),
    url(r'^(?P<pk>\d+)/$', FlightApiDetailView.as_view(), name='flight_detail'),
    url(r'^(?P<pk>\d+)/update/$', FlightApiUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', FlightApiDestroyView.as_view(), name='delete')
]
