from rest_framework import serializers
from django.contrib.auth import get_user_model


from transactions.models import Balance, TransactionHistory
from product.models import Car


User = get_user_model()


class BalanceCreateSerializer(serializers.Serializer):


    class Meta:

        model = Balance
        
        fields = '__all__'
        read_only_fields = ['user']


  
    def save(self, **kwargs):
        user = self.context.get('request').user
        balance_exists = Balance.objects.filter(user=user).exists()

        if balance_exists:
            raise serializers.ValidationError('you already have a balance account')
        self.validated_data['user'] = user
        return super().save(**kwargs)
    


class BalanceDepositeSerializer(serializers.Serializer):

    deposit = serializers.DecimalField(max_digits=9, decimal_places=2)


    class Meta:
        model = Balance
        
        fields = '__all__'
        read_only_fields = ['user']

    def update(self, instance, validated_data):
        deposit = validated_data.pop('deposit')
        instance.balance += deposit
        instance.save()
        return instance


    def partial_update(self, instance, validated_data):
        return self.update(instance, validated_data)
    


class TransactionSerializer(serializers.Serializer):

    username = serializers.CharField()
    product = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=9, decimal_places=2)
    
    class Meta:
        
        fields = '__all__'
        read_only_fields = ['username', 'price']

    
    def create(self, validated_data):
        username = self.context.get('request').user.username
        product = Car.objects.get(id=product)
        product_price = product.price
        user = User.objects.get(username=username)
        balance = user.balance.first()
        balance.total_balance -= product_price
        balance.save()

        transaction = TransactionHistory.objects.create(
            user=user,
            product=product,
            price=product_price
        )
        return transaction

