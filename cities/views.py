from django.views.generic import TemplateView, ListView
from django.db.models import Q  # new

from .models import City


class HomePageView(TemplateView):
    template_name = "home.html"


class SearchResultsView(ListView):
    model = City
    template_name = "search_results.html"

    def get_queryset(self):  # new
        return City.objects.filter(
            Q(name__icontains="ANDORRA") | Q(state__icontains="AD")
        )
