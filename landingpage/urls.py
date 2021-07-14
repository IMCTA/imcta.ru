from django.urls import path

from . import views

app_name = "landingpage"
urlpatterns = [
    path(route="", view=views.LandingPageView.as_view(), name="front"),
]
