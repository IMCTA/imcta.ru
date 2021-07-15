from django.urls import path

from . import views

app_name = "frontpage"
urlpatterns = [
    path(route="", view=views.FrontPageView.as_view(), name="front"),
]
