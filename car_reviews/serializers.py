from rest_framework import serializers


from car_reviews.models import Comment, Rating, Saved


class AbstractListSerializer(serializers.ListSerializer):
    pass


class CommentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Comment
        fields = ['car', 'text', 'created_at']
        
        read_only_fields = ['user', 'created_at',]
    

    def save(self, **kwargs):
        user = self.context.get('request').user
        self.validated_data['user'] = user
        return super().save(**kwargs)


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['car'] = instance.car.brand
        representation['user'] = instance.user.username
        return representation
 
 
    list_serializer_class = AbstractListSerializer



class SavedSerializer(serializers.ModelSerializer):
  

    class Meta:

        model = Saved
        fields = '__all__'
        read_only_fields = ['user']


    def validate(self, attrs):
        user = self.context.get('request').user
        car = attrs.get('car')
        saved = Saved.objects.filter(user=user, car=car)

        if saved.exists():
            raise serializers.ValidationError('You already saved this product')
        
        return super().validate(attrs)


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.username
        representation['car'] = instance.car.brand
        return representation
    

    def save(self, **kwargs):
        user = self.context.get('request').user
        self.validated_data['user'] = user
        return super().save(**kwargs)
    

    list_serializer_class = AbstractListSerializer



class RatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rating
        fields = '__all__'
        read_only_fields = ['user']
    

    def save(self, **kwargs):
        user = self.context.get('request').user
        self.validated_data['user'] = user
        return super().save(**kwargs)


    def validate(self, attrs):
        user = self.context.get('request').user
        car = attrs.get('car')
        rate = Rating.objects.filter(user=user, car=car)
        if rate.exists():
            raise serializers.ValidationError('Rate already exists')
        return super().validate(attrs)


    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['user'] = instance.user.username
        representation['car'] = instance.car.brand
        return representation
