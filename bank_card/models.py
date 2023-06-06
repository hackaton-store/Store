from django.db import models
from django.core.validators import MaxValueValidator

class BankCard(models.Model):
    card_holder = models.ForeignKey('account.User', on_delete=models.CASCADE)
    card_number = models.BigIntegerField()
    cvv = models.IntegerField(validators=[MaxValueValidator(999)])
