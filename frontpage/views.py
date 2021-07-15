from django.views.generic.base import TemplateView

from .models import FrontPage


class FrontPageView(TemplateView):

    template_name = "frontpage/frontpage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["frontpage_data"] = FrontPage.objects.get()
        return context
