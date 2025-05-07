from rest_framework import serializers
from .models import editorial

class editorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = editorial
        fields = '__all__'