from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import TransactionSerializer
from .models import TransactionHistory

class TransactionView(APIView):
   
    permission_classes = [IsAuthenticated]


    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            transaction = serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

   
    def get(self, request, transaction_id=None):
        if transaction_id:

            transaction = TransactionHistory.objects.filter(id=transaction_id, user=request.user).first()
            if transaction:
                serializer = TransactionSerializer(transaction)
                return Response(serializer.data)
            else:
                return Response({'error': 'Транзакция не найдена'}, status=404)
        else:

            if request.user.is_staff:
                transactions = TransactionHistory.objects.all()
                serializer = TransactionSerializer(transactions, many=True)
                return Response(serializer.data)
            else:
                return Response({'error': 'Доступ запрещен'}, status=403)