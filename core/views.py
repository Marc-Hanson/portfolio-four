from django.shortcuts import render, redirect, get_object_or_404
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
    paginate_by = 3


class ProductList(generic.ListView):
    model = Product
    queryset = Product.objects.order_by('title')
    template_name = 'products.html'


def LeaveReview(request, *args, **kwargs):
    if request.method == 'POST':
        title = request.POST['title']
        stars = request.POST['stars']
        content = request.POST['content']
        author = request.user

        new_review = Review(title=title, stars=stars, content=content, author=author, approved=False)
        new_review.save()

        return render(request, 'your_review.html', {'title': title,'content': content,})


def DeleteReview(request, LeaveReview):
    if request.method == 'POST':
        new_review = get_object_or_404(LeaveReview)
        if new_review.author == request.user:
            new_review.delete()
            return redirect("home")
