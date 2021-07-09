from rest_framework.serializers import ModelSerializer
from .models import Plays


class PlaysSerializer(ModelSerializer):
    class Meta:
        model = Plays
        fields = "__all__"
