from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='balance')
    total_balance = models.DecimalField(max_digits=9, decimal_places=2)





class TransactionHistory(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    transaction_time = models.DateTimeField(auto_now_add=True)

