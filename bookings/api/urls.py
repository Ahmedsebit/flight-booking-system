from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BookingApiListView, BookingAPICreateView, BookingApiDetailView, BookingApiDestroyView, BookingApiUpdateView, BookingApiCustomerListView

urlpatterns = [
    path('', BookingApiListView.as_view(), name='api_booking'),
    path('customer/', BookingApiCustomerListView.as_view(), name='api_booking_customer'),
    url(r'^create$', BookingAPICreateView.as_view(), name='api_booking_create'),
    url(r'^(?P<pk>\d+)/$', BookingApiDetailView.as_view(), name='api_booking_detail'),
    url(r'^(?P<pk>\d+)/delete$', BookingApiDestroyView.as_view(), name='api_booking_destroy'),
    url(r'^(?P<pk>\d+)/update$', BookingApiUpdateView.as_view(), name='api_booking_update'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
