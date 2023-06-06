from rest_framework.viewsets import ModelViewSet

from product.models import Car
from product.serializers import CarSerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
