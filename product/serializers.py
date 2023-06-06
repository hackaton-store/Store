from rest_framework.serializers import ModelSerializer
from product.models import Car
from django_filters import rest_framework as filters



class CarSerializer(ModelSerializer):

    class Meta:
        model = Car
        # fields = '__all__'
        exclude = ['status']
        

    # def to_representation(self, instance: Car):
    #     representation = super().to_representation(instance)


class CarFilter(filters.FilterSet):
    status = filters.CharFilter(field_name='status', lookup_expr='exact')

    class Meta:
        model = Car
        fields = ['status']
        