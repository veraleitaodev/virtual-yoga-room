from django.test import TestCase
from .models import Blog, Comment


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        blog1 = Blog.objects.create(
            title='Test blog post', content='Test content', date='2020-06-10')
        comment = Comment.objects.create(
            blog=blog1, body='test body comment',
            name='test', date='2020-06-10')
        self.assertFalse(blog1.author)
        self.assertFalse(comment.active)
