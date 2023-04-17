from rest_framework.viewsets import ModelViewSet
from .models import Flight
from .serializers import FlightSerializer
from .permissions import IsAdminOrReadOnly

# Create your views here.


class FlightView(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAdminOrReadOnly]
