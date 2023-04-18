from rest_framework.viewsets import ModelViewSet
from .models import Flight, Reservation
from .serializers import FlightSerializer, ReservationsSerializer
from .permissions import IsAdminOrReadOnly
from datetime import date, datetime

# Create your views here.


class FlightView(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        current_date = date.today()

        if not self.request.user.is_staff:
            queryset = Flight.objects.filter(departure_date__gt=current_date)
            if Flight.objects.filter(
                    departure_date=current_date):
                query_2 = Flight.objects.filter(
                    departure_date=current_date).filter(
                    departure_time__gt=current_time)
                queryset = queryset.union(query_2)

        return queryset


class ReservationView(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationsSerializer

    def get_queryset(self):
        queryset = self.queryset
        if not self.request.user.is_staff:
            queryset = Reservation.objects.filter(user=self.request.user)

        return queryset
