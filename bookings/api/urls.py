from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BookingApiListView, BookingAPICreateView, BookingApiDetailView, BookingApiDestroyView, BookingApiUpdateView, BookingApiCustomerListView

urlpatterns = [
    path('', BookingApiListView.as_view(), name='booking'),
    path('customer/', BookingApiCustomerListView.as_view(), name='booking_customer'),
    path('create/', BookingAPICreateView.as_view(), name='booking_create'),
    url(r'^(?P<pk>\d+)/$', BookingApiDetailView.as_view(), name='booking_detail'),
    url(r'^(?P<pk>\d+)/delete$', BookingApiDestroyView.as_view(), name='booking_destroy'),
    url(r'^(?P<pk>\d+)/update$', BookingApiUpdateView.as_view(), name='booking_update'),
    # url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='details'),
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete')
]

urlpatterns = format_suffix_patterns(urlpatterns)
