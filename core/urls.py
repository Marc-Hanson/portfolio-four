from core import views
from django.urls import path
from django.views.generic import RedirectView
from .views import LeaveReview


urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('about/', views.ReviewList.as_view(), name='about'),
    path('products/', views.ProductList.as_view(), name='products'),
    path('about/LeaveReview', RedirectView.as_view(url='/about/'), name='leave_review'),
]
