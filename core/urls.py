from core import views
from django.urls import path


urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('about/', views.ReviewList.as_view(), name='about'),
    path('products/', views.ProductList.as_view(), name='products'),
    path('review/', views.LeaveReview, name='leave_review'),
]
