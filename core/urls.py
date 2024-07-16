from django.urls import path
from .views import DepositMoneyView

urlpatterns = [
    path('login/', DepositMoneyView.as_view(), name='Deposit'),

]