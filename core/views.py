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
    paginate_by = 2


class ProductList(generic.ListView):
    model = Product
    queryset = Product.objects.order_by('title')
    template_name = 'products.html'


def LeaveReview(request):
    if request.method == 'POST':
        title = request.POST['title']
        stars = request.POST['stars']
        content = request.POST['content']
        author = request.user
        user_review = Review(title=title, stars=stars, content=content,
                             author=author, approved=False)
        user_review.save()
        return render(request, 'your_review.html',
                      {'title': title, 'content': content})


def UpdateReview(request):
    if request.method == 'GET':
        user_review = get_object_or_404(Review, author=request.user)
        title = user_review.title
        content = user_review.content
        return render(request, 'your_review.html', {'title': title,
                      'content': content})

    elif request.method == 'POST':
        user_review = get_object_or_404(Review, author=request.user)
        if user_review.author == request.user:
            user_review.delete()
            title = request.POST['title']
            stars = request.POST['stars']
            content = request.POST['content']
            author = request.user
            user_review = Review(title=title, stars=stars, content=content,
                                 author=author, approved=False)
            user_review.save()
            return render(request, 'your_review.html', {'title': title,
                          'content': content})
        else:
            return redirect('home')


def DeleteReview(request):
    user_review = get_object_or_404(Review, author=request.user)
    if user_review.author == request.user:
        user_review.delete()
        return redirect('home')
    else:
        return redirect('home')


def return_404(request, exception):
    return render(request, "errors/404.html", {})


def return_500(request, exception=None):
    return render(request, "errors/500.html", {})


def return_403(request, exception=None):
    return render(request, "errors/403.html", {})


def return_400(request, exception=None):
    return render(request, "errors/400.html", {})
