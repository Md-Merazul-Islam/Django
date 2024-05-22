
from django.db import models
from django.contrib.auth.models import User
from .constants import TRANSACTION_TYPE

class Transaction(models.Model):
    user = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits=12)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.user.username} - {self.amount} ({self.transaction_type})"
