# admin.py

from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'balance_after_transaction', 'transaction_type', 'timestamp']
    list_filter = ['user', 'transaction_type']
    search_fields = ['user__username', 'amount']
    readonly_fields = ['balance_after_transaction', 'timestamp']
