from django.conf.urls import url
from .views import CustomUserApiUpdateView, UserApiDetailListView

urlpatterns = [
    url(r'^$', UserApiDetailListView.as_view(), name='user_list'),
    url(r'^(?P<pk>\d+)/update/$', CustomUserApiUpdateView.as_view(), name='update'),
]
