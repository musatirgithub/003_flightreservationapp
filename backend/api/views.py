from rest_framework.viewsets import ModelViewSet
from .models import Flight, Reservation
from .serializers import FlightSerializer, ReservationsSerializer
from .permissions import IsAdminOrReadOnly

# Create your views here.


class FlightView(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAdminOrReadOnly]


class ReservationView(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationsSerializer

    def get_queryset(self):
        return super().get_queryset()
