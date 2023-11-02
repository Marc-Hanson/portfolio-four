from . import views
from django.urls import path


urlpatterns = [
    path('', views.EventList.as_view(), name="home"),
    path('about/', views.ReviewList.as_view(), name="about")
]
