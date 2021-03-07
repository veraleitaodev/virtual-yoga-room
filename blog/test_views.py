from django.test import TestCase
from .models import Blog, Comment


class TestViews(TestCase):

    def test_get_blogs(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_get_blog(self):
        blog = Blog.objects.create(
            title='Test blog post', content='Test content', date='2020-06-10')
        response = self.client.get(f'/blog/{blog.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog-details.html')

    def test_can_add_comment(self):
        blog = Blog.objects.create(
            title='Test blog post', content='Test content', date='2020-06-10')
        response = self.client.post(f'/blog/{blog.id}/', {
            'body': 'Test comment body', 'name': 'test', 'active': False})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog-details.html')
