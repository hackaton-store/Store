from rest_framework import serializers

from bank_card.models import BankCard

class BankCardSerializer(serializers.ModelSerializer):
     
    class Meta:

        model = BankCard
        fields = '__all__'

        extra_kwargs = {
                'card_holder': {'read_only': True},
                'balance': {'read_only': True}}


    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['card_holder'] = user
        return super().create(validated_data)
    
