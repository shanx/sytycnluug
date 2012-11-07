from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.crypto import get_random_string
from django.views.generic import  View, ListView
from django.db.models import Avg, Count

from sytycnluug.ratezzz.models import Talk, Rating

RATER_COOKIE = 'rater_id'


class TalkView(View):
    def get(self, request):
        rater_id = request.COOKIES.get(RATER_COOKIE, get_random_string())

        context = {
            'ratings': Rating.objects.filter(rater_id=rater_id),
            'unrated_talks': Talk.objects.exclude(rating__rater_id=rater_id)
        }

        response = render_to_response('ratezzz/talk_list.html',
            context, context_instance=RequestContext(request))
        response.set_cookie(RATER_COOKIE, rater_id)
        return response

    def post(self, request, pk):
        rater_id = request.COOKIES.get(RATER_COOKIE)

        talk = Talk.objects.get(pk=pk)
        rating, is_created = talk.rating_set.get_or_create(rater_id=rater_id,
            defaults={'rating': request.POST['rating']})

        if not is_created:
            rating.rating = request.POST['rating']
            rating.save()

        return HttpResponse()


class OverallView(ListView):
    context_object_name = "overall_talk_list"
    template_name = "ratezzz/overall_talk_list.html"
    queryset = Talk.objects.annotate(Avg('rating__rating'),
        Count('rating')).order_by('-rating__rating__avg', '-rating__count')
