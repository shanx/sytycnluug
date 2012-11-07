from django.conf.urls import patterns, url

from .views import TalkView, OverallView

urlpatterns = patterns('',
    url(r'^$', TalkView.as_view(), name='talks.list'),
    url(r'^overall/$', OverallView.as_view(), name='talks.overall'),
    url(r'^(?P<pk>\d+)/$', TalkView.as_view(), name='talks.rate'),
)
