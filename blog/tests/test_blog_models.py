from mixer.backend.django import mixer
import pytest

@pytest.mark.django_db
class TestModels:
    def test_blog_is_post_production_completed(self):
        blog = mixer.blend('blog.Blog', content='Sample Content')
        assert blog.is_post_production_completed == True
        
    def test_blog_is_not_post_production_completed(self):
        blog = mixer.blend('blog.Blog', content='')
        assert blog.is_post_production_completed == False