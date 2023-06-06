from rest_framework import routers

from bank_card.views import BankCardViewSet

router = routers.DefaultRouter()
router.register('card', BankCardViewSet, basename='bank_card')

urlpatterns = router.urls