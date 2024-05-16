from django.contrib import admin

# Register your models here.
from .models import Transaction,Bank

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'balance_after_transaction',
                    'transaction_type', 'loan_approve']

    def save_model(self, request, obj, form, change):
        obj.account.balance += obj.amount
        obj.balance_after_transaction = obj.account.balance
        obj.account.save()
        super().save_model(request, obj, form, change)



@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['id','is_bankrupt']
    list_editable =['is_bankrupt']