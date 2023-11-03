from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from core.models import Event, Review, Product


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by('date')
    template_name = 'index.html'


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.order_by('-created_on')
    template_name = 'about.html'
    paginate_by = 1


class ProductList(generic.ListView):
    model = Product
    queryset = Event.objects.order_by('title')
    template_name = 'products.html'
    paginate_by = 2
