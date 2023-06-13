from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from .serializers import UserSerializer
from core.models import User
from .authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        if data["password"] != data["password_confirm"]:
            raise exceptions.APIException("Password do not match!")
        data["is_agent"] = 0
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPIView(APIView):
    def post(sefl, request):
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()
        if user is None:
            raise exceptions.AuthenticationFailed("User Not Found")

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed("incorrect password")

        token = JWTAuthentication.generate_jwt(user.id)
        response = Response()
        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {"message": "success"}
        return response


class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)
    
class LogoutAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        response = Response()
        response.delete_cookie(key='jwt')
        response.data = {'message': 'success'}
        return response
    
class ProfileInfoAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class ProfilePasswordAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user
        data = request.data
        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Password do not match')
        user.set_password(data['password'])
        user.save()
        return Response(UserSerializer(user).data)