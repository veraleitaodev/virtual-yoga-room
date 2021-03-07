from django.test import TestCase


class TestViews(TestCase):

    def test_get_blogs(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    #def test_get_blog(self):
    
   # def test_get_comments(self):

   # def test_can_add_comment(self):
    

