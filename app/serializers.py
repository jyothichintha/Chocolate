from rest_framework import serializers

from app.models import *
class ChocolateMS(serializers.ModelSerializer):
    class Meta:
        model=Chocolate
        fields="__all__"