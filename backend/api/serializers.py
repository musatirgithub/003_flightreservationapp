from rest_framework import serializers
from .models import Flight, Reservation, Passenger


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
    user_id = serializers.IntegerField()
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
