from django.urls import path

from .views import TourDetailView, TourListView

app_name = "tours"
urlpatterns = [
    path("", view=TourListView.as_view(), name="list"),
    path("<int:pk>/", view=TourDetailView.as_view(), name="detail"),
]
