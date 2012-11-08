from django.test import TestCase

from .models import Talk


class TalkViewTests(TestCase):
    rater_id = 'test_rater'

    def setUp(self):
        self.talk = Talk.objects.create(name='My preciousssss...', speakers='Gollum')
        self.client.cookies['rater_id'] = self.rater_id

    def test_index_redirects_to_rate(self):
        # A request to the root url is redirected to ratezzz index url
        self.assertRedirects(self.client.get('/'), '/ratezzz/')

    def test_rate_talk(self):
        # Talk doesn't have a rating
        self.assertFalse(self.talk.rating_set.exists())

        # Sending post request to talk  at ratezzz/1/ creates a rating for this talk
        self.client.post('/ratezzz/1/', data={'rating': 5})
        rating = self.talk.rating_set.get()
        self.assertEqual(rating.rating, 5)

        # Sending another post updates the value
        self.client.post('/ratezzz/1/', data={'rating': 2})
        rating = self.talk.rating_set.get()
        self.assertEqual(rating.rating, 2)


class OverallViewTests(TestCase):
    def test_overall(self):
        # Sanity check that no talks are returned when none exist
        response = self.client.get('/ratezzz/overall/')
        self.assertFalse(response.context_data['overall_talk_list'].exists())

        # Creating a talk with ratings should return correct numbers
        talk = Talk.objects.create(name='My preciousssss...', speakers='Gollum')
        talk.rating_set.create(rater_id='rater1', rating=4)
        talk.rating_set.create(rater_id='rater2', rating=2)

        response = self.client.get('/ratezzz/overall/')
        returned_talk = response.context_data['overall_talk_list'][0]
        self.assertEqual(returned_talk.name, 'My preciousssss...')
        self.assertEqual(returned_talk.rating__rating__avg, 3)
        self.assertEqual(returned_talk.rating__count, 2)
