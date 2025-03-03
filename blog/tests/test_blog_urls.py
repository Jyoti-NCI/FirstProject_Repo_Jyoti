from django.urls import reverse, resolve
from blog import views

class TestUrls:
    def test_detail_url(self):
        path = reverse('blog:index', kwargs={})
        assert resolve(path).view_name == 'blog:index'