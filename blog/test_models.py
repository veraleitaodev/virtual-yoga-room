from django.test import TestCase
from .models import Blog, Comment


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        blog = Blog.objects.create(
            title='Test blog post', content='Test content', date='2020-06-10')
        blog_pk = Blog.objects.get(pk=1).pk
        comment = Comment.objects.create(
            blog=blog_pk, body='test body comment',
            name='test', date='2020-06-10')
        self.assertFalse(blog.author)
        self.assertFalse(comment.active)
