from django.conf.urls import patterns, url

from .views import TalkView

urlpatterns = patterns('',
    url(r'^$', TalkView.as_view(), name='talks.list'),
    url(r'^(?P<pk>\d+)/$', TalkView.as_view(), name='talks.rate'),
)
