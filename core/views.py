<<<<<<< HEAD
=======
from django.shortcuts import render
>>>>>>> 783a447edc49da106769be58ac8d225c43370247
from django.views import generic, View
from django.views.generic import ListView
from .models import Event, Review

class Home(View):
    pass


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by('date')
    template_name = 'index.html'


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.order_by('-created_on')
    template_name = 'about.html'
    #paginate_by = 1
