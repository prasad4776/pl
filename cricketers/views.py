from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Plays
from .serailizers import PlaysSerializer


# Create your views here.


class AllPlayersView(ListCreateAPIView):
    queryset = Plays.objects.all()
    serializer_class = PlaysSerializer
