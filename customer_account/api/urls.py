from django.conf.urls import url
from .views import CustomerAccountApiListView

urlpatterns = [
    url(r'^$', CustomerAccountApiListView.as_view(), name='customers'),
    # url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='details'),
    # url(r'^create/$', TweetCreateView.as_view(), name='create'),
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete')
]
