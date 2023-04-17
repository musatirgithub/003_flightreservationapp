from rest_framework.serializers import ModelSerializer
from .models import Flight


class FlightSerializer(ModelSerializer):

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
