from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q


from permissions.permissions import IsOwner, IsModeratorOrIsAdminUser, IsOwnerOrIsModeratorOrIsAdminUser
from product.models import Car
from product.serializers import CarSerializer, OneCarSeralizer
from .utils import CarFilter



def check_user(request: Request):
    if not request.user.is_anonymous:
        if (request.user.is_staff or request.user.is_moderator):
            return True
        

class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    

    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_class = CarFilter

    filterset_fields = ['brand', 'color']
    search_fields = ['title', 'description']
    ordering_fields = ['price']


    def list(self, request: Request, *args, **kwargs):
        queryset = self.filter_queryset(Car.objects.filter(status='published'))
        check = check_user(request)
        if check:
            queryset = Car.objects.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        

    def retrieve(self, request, *args, **kwargs):
        
        self.serializer_class = OneCarSeralizer
        return super().retrieve(request, *args, **kwargs)    


    def get_permissions(self):
        if self.request.data.get('status'):
            if self.request.method in ['GET', 'POST', 'PATCH', 'PUT', 'DELETE']:
                self.permission_classes = [IsModeratorOrIsAdminUser]
        else:
            if self.request.method == "GET":
                self.permission_classes = [AllowAny]
            elif self.request.method == "POST":
                self.permission_classes = [IsAuthenticated]
            elif self.request.method in ['DELETE', 'PATCH', 'PUT']:
                
                self.permission_classes = [IsOwnerOrIsModeratorOrIsAdminUser]

        return super().get_permissions()
    

    


