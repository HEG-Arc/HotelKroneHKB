from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.base import RedirectView

from . import models


class Zimmer(DetailView):
    model = models.Student
    slug_field = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_orte'] = models.POI.objects.filter(media__student=self.get_object()).first()
        context['second_orte'] = models.POI.objects.filter(media__student=self.get_object()).last()
        context['artworks'] = models.Media.objects.filter(student=self.get_object(),
                                                          display_in_zimmer=True).order_by("order", "name")

        students = models.Student.objects.all()
        for i, student in enumerate(students):
          if student == self.get_object():
            try:
              prev = students[i-1]
            except:
              try:
                prev = students[len(students)-1]
              except:
                prev = None
            try:
              next = students[i+1]
            except:
              try:
                next = students[0]
              except:
                next = None
        context['prev_student'] = prev
        context['next_student'] = next

        return context


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
        context['orte_list'] = models.Orte.objects.exclude(pk=self.get_object().id)
        return context
