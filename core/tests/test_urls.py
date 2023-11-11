from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import EventList, ReviewList, ProductList
from core.views import LeaveReview, UpdateReview, DeleteReview


class TestUrls(SimpleTestCase):

    def test_home_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, EventList)

    def test_about_url(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func.view_class, ReviewList)

    def test_products_url(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func.view_class, ProductList)

    def test_leave_review_url(self):
        url = reverse('leave_review')
        self.assertEquals(resolve(url).func, LeaveReview)

    def test_update_review_url(self):
        url = reverse('update_review')
        self.assertEquals(resolve(url).func, UpdateReview)

    def test_delete_review_url(self):
        url = reverse('delete_review')
        self.assertEquals(resolve(url).func, DeleteReview)
