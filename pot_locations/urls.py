from django.urls import path
from . import views

urlpatterns = [
    path("", views.pot_locations, name="pot_locations")
]
