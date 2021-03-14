from django.test import TestCase
from core.models import UrlData
import random, string

class UrlViewsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        url = 'https://docs.djangoproject.com/en/3.1/ref/forms/fields/#urlfield'
        slug = ''.join(random.choice(string.ascii_letters)
                           for x in range(10))
        UrlData.objects.create(url=url, slug=slug)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/main')
        self.assertEqual(resp.status_code, 200)
        
    def test_view_url_exists_at_desired_location_detail(self):
        resp = self.client.get('/detail/1')
        self.assertEqual(resp.status_code, 200)