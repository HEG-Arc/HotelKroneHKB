from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.base import RedirectView

from . import models


class Zimmer(DetailView):
    model = models.Student
    slug_field = "slug"


class Orte(DetailView):
    model = models.Orte
    slug_field = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = models.Student.objects.all()
        return context


class POI(DetailView):
    model = models.POI


class HotelKrone(DetailView):

    def get_object(self, *args, **kwargs):
        return models.Orte.objects.filter(entrance=True).first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = models.Student.objects.all()
        return context
