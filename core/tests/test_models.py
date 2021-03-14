from django.test import TestCase
from core.models import UrlData
import random
import string

class UrlDataModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        url = 'https://docs.djangoproject.com/en/3.1/ref/forms/fields/#urlfield'
        slug = ''.join(random.choice(string.ascii_letters)
                           for x in range(10))
        UrlData.objects.create(url=url, slug=slug)

    def test_url_max_length(self):
        obj = UrlData.objects.get(id=1)
        max_length = obj._meta.get_field('url').max_length
        self.assertEquals(max_length,200)

    def test_object_name_is_right(self):
        obj = UrlData.objects.get(id=1)
        expected_object_name = f"Short Url for: {obj.url} is {obj.slug}"
        self.assertEquals(expected_object_name, str(obj))
