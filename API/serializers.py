from rest_framework import serializers
from .models import NajotTalim


class NajotTalimSerializer(serializers.ModelSerializer):
    class Meta:
        model = NajotTalim
        fields = '__all__'