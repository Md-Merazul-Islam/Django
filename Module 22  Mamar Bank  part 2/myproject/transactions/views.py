from django.http import HttpRequest
from typing import Any
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction
from . forms import DepositForm ,WithdrawForm, LoanRequestForm
from .constants import DEPOSIT,WITHDRAWAL,LOAN,LOAN_PAID
from django.contrib import messages
class TransactionCreateMixin(LoginRequiredMixin,CreateView):
    template_name = ''
    model = Transaction
    title = ''
    success_url=''
    
    def get_form_kwargs(self) :
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account,
        })
        return kwargs
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context.update({
            'title':self.title
        })
        
        
        
class DepositMoneyView(TransactionCreateMixin):
    form_class= DepositForm
    title = 'Deposit'
    
    def get_initial(self) :
        initial = {'transaction_type': DEPOSIT}
        return initial
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        account.save(
            update_fields=[
                'balance'
            ]
        )
        
        messages.success(self.request, f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully')
        
        return super().form_valid(form)


class WithdrawMoneyView(TransactionCreateMixin):
    form_class =WithdrawForm
    title ='Withdraw'
    
    def get_initial(self) :
        initial ={'transaction_type': WITHDRAWAL}
        return initial
    def form_valid(self, form):
        amount= form.cleaned_data.get('amount')
        account= self.request.usr.account
        account.balance -= amount
        account.save(
            update_fields=[
                'balance'
            ]
        )    
        messages.success(self.request, f'{"{:,.2f}".format(float(amount))}$ was withdraw from your account successfully')
          
        return super().form_valid(form)
    
class LoanRequestView(TransactionCreateMixin):
    form_class = LoanRequestForm
    title = 'Request for loan'
    
    def get_initial(self):
        initial ={'transaction_type': LOAN}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        current_loan_count = Transaction.objects.filter(account = self.request.user.account, transaction_type=3 , loan_approve=True).count()
        if current_loan_count>=3:
            return HttpRequest('You have cross the loan limits')
        messages.success(self.request , f'loan request for {"{:,.2f}".format(float(amount))}$  submitted successfully')
        
        
        return super().form_valid(form)
    