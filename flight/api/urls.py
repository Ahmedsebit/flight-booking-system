from django.conf.urls import url
from .views import FlightApiListView,  FlightAPICreateView

urlpatterns = [
    url(r'^$', FlightApiListView.as_view(), name='flight'),
    url(r'^create/$', FlightAPICreateView.as_view(), name='flight_create'),
    # url(r'^create/$', TweetCreateView.as_view(), name='create'),
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete')
]
