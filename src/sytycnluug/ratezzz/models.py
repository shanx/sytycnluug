from django.contrib.sessions.models import Session
from django.db import models

class Talk(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    speakers = models.CharField(max_length=200)

    def __unicode__(self):
        return u'{0} by {1}'.format(self.name, self.speakers)

    def get_absolute_url(self):
        return '/ratezzz/{0}/'.format(self.pk)

class Rating(models.Model):
    talk = models.ForeignKey(Talk)
    rater_id = models.CharField(max_length=12)
    rating = models.PositiveSmallIntegerField()

    class Meta:
        # Every rater can only vote once per talk
        unique_together = ('talk', 'rater_id')

    def __unicode__(self):
        return u'{0} by {1}'.format(self.rating, self.rater_id)