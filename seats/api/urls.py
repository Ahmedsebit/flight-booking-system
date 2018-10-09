from django.conf.urls import url
from .views import SeatApiListView, SeatApiDetailView, SeatApiDestroyView, SeatApiUpdateView, SeatApiCreateView

urlpatterns = [
    url(r'^$', SeatApiListView.as_view(), name='seat_list'),
    url(r'^/create$', SeatApiCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/delete/$', SeatApiDestroyView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/detail/$', SeatApiDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', SeatApiUpdateView.as_view(), name='update'),
]
