from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from rest_framework import generics

from product.models import Car
from product.serializers import CarSerializer, CarFilter



class CarViewSet(ModelViewSet):
    queryset = Car.objects.filter(status="published")
    serializer_class = CarSerializer
    # filterset_class = CarFilter


# class CarFilter(filters.FilterSet):
#     min_price = filters.NumberFilter(field_name="status", lookup_expr='exact')

#     class Meta:
#         model = Car
#         fields = ['status']

# class CarViewSet(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_class = CarFilter