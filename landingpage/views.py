from django.views.generic.base import TemplateView

from .models import LandingPage


class LandingPageView(TemplateView):

    template_name = "landingpage/landingpage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["landingpage_data"] = LandingPage.objects.get(pk=1)
        return context
