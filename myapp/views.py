from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer, Transaction
from .serializers import CustomerSerializer, TransactionSerializer

class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        customer_serializer = CustomerSerializer(customers, many=True)
        return Response({'customers': customer_serializer.data})

class TransactionListView(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        transaction_serializer = TransactionSerializer(transactions, many=True)
        return Response({'transactions': transaction_serializer.data})