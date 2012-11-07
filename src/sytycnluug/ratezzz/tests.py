from django.test import TestCase

from .models import Talk


class TalkViewTests(TestCase):
    rater_id = 'test_rater'

    def setUp(self):
        self.talk = Talk.objects.create(name='My preciousssss...', speakers='Gollum')
        self.client.cookies['rater_id'] = self.rater_id

    def test_index_redirects_to_rate(self):
        self.assertRedirects(self.client.get('/'), '/ratezzz/')

    def test_rate_talk(self):
        # Talk 2 doesn't have a rating
        self.assertFalse(self.talk.rating_set.exists())

        # Sending post request to /2/ creates a rating for talk 2
        response = self.client.post('/ratezzz/1/', data={'rating': 5})
        rating = self.talk.rating_set.get()
        self.assertEqual(rating.rating, 5)

        # Sending another post updates the value
        response = self.client.post('/ratezzz/1/', data={'rating': 2})
        rating = self.talk.rating_set.get()
        self.assertEqual(rating.rating, 2)

