from django.test import TestCase
from core.forms import UrlForm

class UrlFormTest(TestCase):

    def test_url_label(self):
        form = UrlForm()
        self.assertTrue(form.fields['url'].label == 'URL')
        
    def test_valid_url(self):
        url = 'https://docs.djangoproject.com/en/3.1/ref/forms/fields/#urlfield'
        form_data = {'url': url}
        form = UrlForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_invalid_url(self):
        url = 'testFalse'
        form_data = {'url': url}
        form = UrlForm(data=form_data)
        self.assertFalse(form.is_valid())
