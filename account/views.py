from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_202_ACCEPTED, HTTP_200_OK 
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from account.serializers import RegistrationSerializer, ActivationSerializer, LoginSerializer, ChangePasswordSerializer, DropPasswordSerializer, ChangeForgottenPassword, UserSerializer


User = get_user_model()

class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)

        return Response({'message': 'Thank you for reqistration, we\'ve sended activation code to your email'})
    

class ActivationView(CreateAPIView):
    serializer_class = ActivationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.activate()
        return Response({'message': 'Account activated successfully'}, status=HTTP_202_ACCEPTED)
    

class LoginView(ObtainAuthToken):
    serializer_class=LoginSerializer

class LogoutView(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request: Request):
        Token.objects.get(user=request.user).delete()
        return Response({'message': 'Logged out'}, status=HTTP_204_NO_CONTENT)
    



class ChangePasswordView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()  # my func in serializers
        return Response({'message': 'password changed successfully'}, status=HTTP_200_OK)




class DropPasswordView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = DropPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_activation_code()
        return Response({'Message': 'Sended activation code'}, status=HTTP_200_OK)
    

class ChangeForgottenPasswordView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = ChangeForgottenPassword(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response({'message': 'Password changed successfully'}, status=HTTP_200_OK)
    

class UserView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response("User not found", status=404)