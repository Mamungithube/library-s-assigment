from django import forms 
from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'amount',
        ]

    def __init__(self, *args, **kwargs):
        self.user_account = kwargs.pop('account') # account value ke pop kore anlam
        super().__init__(*args, **kwargs)
    

    def save(self, commit=True):
        self.instance.account = self.user_account
        return super().save(commit=commit)
    


class DepositForm(TransactionForm):
    def clean_amount(self):
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount')
        if amount < min_deposit_amount :
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount} $'
            )
        
        return amount
    