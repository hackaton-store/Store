from rest_framework.serializers import ModelSerializer
from product.models import Car
from django_filters import rest_framework as filters



class CarSerializer(ModelSerializer):

    class Meta:
        model = Car
        # fields = '__all__'
        fields = [
            'title', 'description',
            'user', 'brand',
            'color', 'release',
            'image'
        ]
        extra_kwargs = {
            'user': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

    def to_representation(self, instance: Car):
        representation = super().to_representation(instance)
        # representation['user'] =
        representation["created_at"] = instance.created_at
        representation["updated_at"] = instance.updated_at
        return representation

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)
    

