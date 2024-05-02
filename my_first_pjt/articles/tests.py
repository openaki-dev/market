# blog/tests.py

from rest_framework.test import APITestCase
from .models import Post
from .serializers import PostSerializer

class PostTest(APITestCase):
    def test_list(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], Post.objects.count())

    def test_detail(self):
        post = Post.objects.first()
        response = self.client.get(f'/posts/{post.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, PostSerializer(post).data)
