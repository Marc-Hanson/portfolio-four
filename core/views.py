from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Event, Review


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by('date')
    template_name = 'index.html'


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.order_by('-created_on')
    template_name = 'about.html'