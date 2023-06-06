from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated


from bank_card.serializers import BankCardSerializer
from bank_card.models import BankCard


class BankCardViewSet(ModelViewSet):
    
    queryset = BankCard.objects.all()
    serializer_class = BankCardSerializer


    def get_permissions(self):
        self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
