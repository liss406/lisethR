from rest_framework import serializers
from .models import Formula1

class Formula1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Formula1
        fields = '__all__'