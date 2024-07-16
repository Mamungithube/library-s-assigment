from .forms import DepositForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Transaction,UserAccount
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

class TransactionCreateMixin(LoginRequiredMixin,CreateView):
    template_name = 'transaction_form.html'
    model = Transaction
    success_url = reverse_lazy('home')
    title = ''

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user_account,created = UserAccount.objects.get_or_create(user=self.request.user)
        kwargs.update({
            'account': user_account,
        })
        return kwargs
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title,

        })
        return context


class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Please Money Deposit'

    
    def form_valid(self,form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        account.save(
            update_fields = [
                'balance',
            ]
        )
        
        messages.success(

            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )
        return super().form_valid(form)