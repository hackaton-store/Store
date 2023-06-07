from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin


from car_reviews.models import Comment, Saved, Rating
from .serializers import CommentSerializer, SavedSerializer, RatingSerializer
from permissions.permissions import IsOwner, IsModerator


class CommentViewSet(ModelViewSet):
   
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]

        else:
            self.permission_classes = [IsOwner]
        return super().get_permissions()
    

class SavedViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = SavedSerializer

    def get_queryset(self):

        return Saved.objects.filter(user=self.request.user)
    

class RatingViewSet(CreateModelMixin, UpdateModelMixin, GenericViewSet):
   
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


    def get_permissions(self):

        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        
        else:
            self.permission_classes = [IsOwner]

        return super().get_permissions()