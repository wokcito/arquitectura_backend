from rest_framework import serializers
from airbnb.models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['address', 'owner', 'price', 'priceBy', 'max_guests', 'description']
