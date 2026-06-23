from rest_framework import serializers
from .models import FactionMember, Faction


class FactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faction
        fields = ['id', 'name']


class FactionMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactionMember
        fields = ['id', 'name', 'role', 'bio', 'faction', 'created_at']