from django.test import TestCase
from core.models import Event, StarRating, Review, Product
from django.contrib.auth.models import User


class TestModels(TestCase):

    def setUp(self):
        self.event1 = Event.objects.create(
            title="test_title",
            location="test_location",
            description="test_description",
            date="2023-11-11 11:11:11"
        )
        self.product1 = Product.objects.create(
            title="test_title",
            description="test_description"
        )
        self.user1 = User.objects.create(
            username="test",
        )
        self.review1 = Review.objects.create(
            title="test_title",
            stars=5,
            content="test_content",
            author=self.user1,
            approved=True
        )

    def test_event_create(self):
        self.assertEquals(self.event1.title, "test_title")
        self.assertEquals(self.event1.location, "test_location")
        self.assertEquals(self.event1.description, "test_description")
        self.assertEquals(self.event1.date, "2023-11-11 11:11:11")

    def test_product_create(self):
        self.assertEquals(self.event1.title, "test_title")
        self.assertEquals(self.event1.description, "test_description")

    def test_review_create(self):
        self.assertEquals(self.review1.title, "test_title")
        self.assertEquals(self.review1.stars, 5)
        self.assertEquals(self.review1.content, "test_content")
