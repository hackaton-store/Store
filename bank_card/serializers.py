from rest_framework import serializers

# from bank_card.models import BankCard

# class BankCardSerializer(serializers.ModelSerializer):
     
#     class Meta:

#         model = BankCard
#         fields = '__all__'

#         extra_kwargs = {
#                 'card_holder': {'read_only': True},
#                 'balance': {'read_only': True}}


#     def create(self, validated_data):
#         user = self.context.get('request').user
#         if BankCard.objects.filter(card_holder=user).exists():
#             raise serializers.ValidationError('you already have a card')
#         validated_data['card_holder'] = user
#         return super().create(validated_data)


# class BankCardDepositeSerializer(serializers.ModelSerializer):
#     deposit = serializers.DecimalField(max_digits=9, decimal_places=2)

#     class Meta:
#         model = BankCard

#         fields = '__all__'

#         read_only_fields = ['id', 'card_holder', 'card_number', 'cvv']


   