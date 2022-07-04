from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from posts.models import Post


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test", num=5)

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test")
        self.assertEqual(self.post.num, 5)

    def test_url_exists_at_correct_location(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "This is a test")
