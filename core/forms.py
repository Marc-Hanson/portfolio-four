from django.forms import ModelForm
from .models import Review, StarRating


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content']
