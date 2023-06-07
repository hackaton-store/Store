from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request

from django_filters import rest_framework as filters

from permissions.permissions import IsOwner, IsModerator
from product.models import Car
from product.serializers import CarSerializer



def check_user(request: Request):
        if not request.user.is_anonymous:
            if (request.user.is_staff or request.user.is_moderator):
                return True


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def list(self, request: Request, *args, **kwargs):
        # queryset = self.filter_queryset(self.get_queryset())
        check = check_user(request)
        queryset = (Car.objects.filter(status='published'))
        if check:
            queryset = Car.objects.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [AllowAny]
        elif self.request.method == "POST":
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsOwner, IsAdminUser, IsModerator]
        return super().get_permissions()
    


