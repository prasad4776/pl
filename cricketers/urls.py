from .views import AllPlayersView
from django.urls import path

urlpatterns = [
    path("all", AllPlayersView.as_view(), name="all_players")
]
