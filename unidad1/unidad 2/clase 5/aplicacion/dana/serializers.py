from rest_framework import serializers
from .models import Dana

class DanaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dana
        fields = "__all__"
        