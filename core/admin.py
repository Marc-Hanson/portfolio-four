from django.contrib import admin
from .models import Event, Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('created_on', 'approved')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = ('date', 'title')
