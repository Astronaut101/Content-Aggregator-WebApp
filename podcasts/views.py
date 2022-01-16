from django.shortcuts import render
from django.views.generic import ListView

from .models import Episode

# Create your views here.
class HomePageView(ListView):
    template_name = "homepage.htm"
    model = Episode

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["episodes"] = Episode.objects.filter().order_by("pub_date")[:10]
        return context