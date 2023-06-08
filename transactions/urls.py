from django.urls import path
from .views import TransactionView


urlpatterns = [
    path('transactions/', TransactionView.as_view(), name='transaction-list'),
    path('transactions/<int:transaction_id>/', TransactionView.as_view(), name='transaction-detail'),
]