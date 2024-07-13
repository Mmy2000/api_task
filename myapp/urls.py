from django.urls import path
from .views import CustomerListView , TransactionListView

urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
]