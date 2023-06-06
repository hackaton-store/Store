from django.db import models
from django.core.validators import MaxValueValidator

class BankCard(models.Model):
    card_holder = models.OneToOneField('account.User', on_delete=models.CASCADE)
    card_number = models.BigIntegerField()
    cvv = models.IntegerField(validators=[MaxValueValidator(999)])
    balance = models.DecimalField(max_digits=9, decimal_places=2, default=0)
