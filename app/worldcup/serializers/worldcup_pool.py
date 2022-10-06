"""Worldcup pools serializers."""

# Django rest framework
from rest_framework import serializers

# Models
from worldcup.models.worldcup_pools import WorldcupPool


class WorldcupPoolModelSerializer(serializers.ModelSerializer):
    """worldcup pool model serializer."""

    class Meta:
        model = WorldcupPool
        fields = '__all__'
        

class CreateWorldcupPoolModelSerializer(serializers.ModelSerializer):
    """Create worldcup pool serializer."""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
     
    class Meta:
        model = WorldcupPool
        fields = '__all__'
        