from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url=reverse_lazy('ratezzz:talks.list'), permanent=False)),
    url(r'^ratezzz/', include('sytycnluug.ratezzz.urls', namespace='ratezzz')),
)