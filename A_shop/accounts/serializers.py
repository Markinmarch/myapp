from rest_framework import serializers

from accounts.models import Profiles

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profiles
        fields = [
            'id',
            'user',
            'text',
            'date',
            'open',
        ]
        read_only_fields = [
            'user',
        ]