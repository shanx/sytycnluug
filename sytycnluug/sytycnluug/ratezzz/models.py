from django.db import models

class Talk(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    speakers = models.CharField(max_length=200)

class Rating(models.Model):
    talk = models.ForeignKey(Talk)
    name = models.CharField(max_length=200)
    rating = models.PositiveSmallIntegerField()