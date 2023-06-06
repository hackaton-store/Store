from rest_framework.serializers import ModelSerializer

from product.models import Car


class CarSerializer(ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'
        

    # def to_representation(self, instance: Car):
    #     representation = super().to_representation(instance)

