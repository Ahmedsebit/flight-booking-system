from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BookingCreateView

urlpatterns = [
    url(r'^(?P<pk>\d+)/create$', BookingCreateView.as_view(), name='booking_create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
