from rest_framework.serializers import ModelSerializer
from product.models import Car
from django_filters import rest_framework as filters
from django.db.models import Avg
from car_reviews.serializers import CommentSerializer



class CarSerializer(ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)


    class Meta:
        model = Car
        # fields = '__all__'
        fields = [
            'title', 'description',
            'price',
            'user', 'brand',
            'color', 'release',
            'image', 'id', 'status',
            'comments'
        ]
        extra_kwargs = {
            'user': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'comments': {'read_only': True},

        }

    def to_representation(self, instance: Car):
        representation = super().to_representation(instance)
        representation['rating'] = round(instance.rates.aggregate(Avg('rate'))['rate__avg'] or 0, 1)
        representation["created_at"] = instance.created_at
        representation["updated_at"] = instance.updated_at
        representation['user'] = instance.user.username
        
        return representation

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        if not self.context["request"].data.get("status"):
            validated_data['status'] = "processing"
        return super().update(instance, validated_data)
    


    