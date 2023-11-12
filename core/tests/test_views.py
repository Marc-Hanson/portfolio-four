from django.test import TestCase, Client, override_settings
from django.urls import reverse
from core.views import Event, Review, Product


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.about_url = reverse('about')
        self.products_url = reverse('products')

    def test_event_list(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_review_list(self):
        response = self.client.get(self.about_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_product_list(self):
        response = self.client.get(self.products_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')
