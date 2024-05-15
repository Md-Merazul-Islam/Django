from django.db import models
from accounts.models import UserBankAccount
from .constants import TRANSACTION_TYPE
from datetime import datetime

class Transaction(models.Model):
    account = models.ForeignKey(UserBankAccount, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits=12)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null=True)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)  # Specify a default value
    load_approve = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['timestamp']
