from django.urls import reverse, resolve
from django.test import TestCase
from movies import views

class TestUrls():
    def test_detail_url(self):
        path = reverse('movies:index', kwargs={})
        assert resolve(path).view_name == 'movies:index'
