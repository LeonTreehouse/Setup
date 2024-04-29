from api.models import Car
from rest_framework import serializers

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("id", "brand")

    def create(self, validated_data):
        car = Car(**validated_data)
        brand = validated_data["brand"]
        car.brand = brand
        car.save()
        return car