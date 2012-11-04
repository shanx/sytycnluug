from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from sytycnluug.ratezzz.models import Talk, Rating

class RatingCreate(CreateView):
    model = Rating

class IndexView(TemplateView):
    template_name = "index.html"