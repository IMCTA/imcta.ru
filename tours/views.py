from django.views.generic import DetailView, ListView

from .models import Tour


class TourListView(ListView):
    model = Tour


class TourDetailView(DetailView):
    model = Tour
