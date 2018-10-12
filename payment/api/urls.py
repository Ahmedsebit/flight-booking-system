from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PaymentAPICreateView, PaymentApiCustomerListView, PaymentApiDestroyView, PaymentApiDetailView, PaymentApiListView, PaymentApiUpdateView

urlpatterns = [
    url(r'^create$', PaymentAPICreateView.as_view(), name='payment_create'),
    path('', PaymentApiListView.as_view(), name='api_booking'),
    url(r'^customer/$', PaymentApiCustomerListView.as_view(), name='api_payment_customer'),
    url(r'^(?P<pk>\d+)/$', PaymentApiDetailView.as_view(), name='api_payment_detail'),
    url(r'^(?P<pk>\d+)/delete$', PaymentApiDestroyView.as_view(), name='api_payment_destroy'),
    url(r'^(?P<pk>\d+)/update$', PaymentApiUpdateView.as_view(), name='api_payment_update'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
