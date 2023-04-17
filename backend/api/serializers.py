from rest_framework import serializers
from .models import Flight, Reservation, Passenger
from django.contrib.auth.models import User


class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "departure_airport",
            "arrival_airport",
            "departure_date",
            "departure_time",
            "company",
        )


class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passenger
        fields = (
            "id",
            "TC_id_number",
            "first_name",
            "last_name",
            "phone",
            "email",
        )


class ReservationsSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer(many=True)
    user = serializers.StringRelatedField()
    flight = serializers.StringRelatedField()
    flight_id = serializers.IntegerField()

    class Meta:
        model = Reservation
        fields = (
            "id",
            "user",
            "user_id",
            "flight",
            "flight_id",
            "passenger",
        )

    def create(self, validated_data):
        passengers = validated_data.pop("passenger")
        validated_data["user_id"] = self.context["request"].user.id
        reservation = Reservation.objects.create(**validated_data)

        for passenger in passengers:
            item = Passenger.objects.create(**passenger)
            reservation.passenger.add(item)

        reservation.save()
        return reservation
