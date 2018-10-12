from django.conf.urls import url
from .views import UserApiListView, CustomUserApiDetailView, CustomUserApiDestroyView, CustomUserApiUpdateView, UserApiDetailListView

urlpatterns = [
    url(r'^$', UserApiDetailListView.as_view(), name='user_list'),
    # url(r'^/detail/$', UserApiDetailListView.as_view(), name='user_details'),
    # url(r'^(?P<pk>\d+)/detail/$', CustomUserApiDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', CustomUserApiUpdateView.as_view(), name='update'),
]
