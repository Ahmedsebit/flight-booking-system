from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PaymentCreateView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', PaymentCreateView.as_view(), name='payment'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
