from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAdminUser
from django.contrib.auth import authenticate
from rest_framework import status
from django.core.mail import send_mail
from random import choice
from .models import Contestant


# Función para el registro global de usuarios
class RegisterContestant(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        data = request.data
        if Contestant.objects.filter(email=data['email']).exists():
            return Response({"error": "Email already exists"}, status=400)
        Contestant.objects.create(
            email=data['email'],
            full_name=data['full_name'],
            phone=data.get('phone', '')
        )
        return Response({"message": "Contestant registered successfully"}, status=201)
    

#Función para verificar email de usuario
class VerifyEmail(APIView):
    def post(self, request):
        token = request.data.get('token')
        password = request.data.get('password')
        if not token:
            return Response({"error": "Token y Contraseña son requeridos"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            contestant = Contestant.objects.get(id=token)
            if not contestant.email_verified:
                contestant.email_verified = True
                contestant.password = make_password(password)
                contestant.save()
                return Response({"message": "Correo verificado y contraseña creada con éxito"})
            else:
                return Response({"error": "Correo ya verificado"}, status=status.HTTP_400_BAD_REQUEST)
        except Contestant.DoesNotExist:
            return Response({"error": "Token no válido"}, status=status.HTTP_400_BAD_REQUEST)
        
#Función para el login
class AdminLogin(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        from django.contrib.auth import get_user_model
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
            if user.check_password(password): 
                if user.is_staff:
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    })
                return Response({"error": "No tienes permisos de administrador."}, status=status.HTTP_403_FORBIDDEN)
            return Response({"error": "Credenciales inválidas."}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({"error": "Credenciales inválidas."}, status=status.HTTP_401_UNAUTHORIZED)

#Función para encontrar un ganador
class GenerateWinner(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        verified_users = Contestant.objects.filter(email_verified=True)

        if not verified_users.exists():
            return Response({"error": "No hay usuarios verificados"}, status=status.HTTP_400_BAD_REQUEST)
        
        winner = choice(verified_users)

        send_mail(
            subject='¡Felicidades! Has ganador el sorteo de San Valentín',
            message='Has sido seleccionado como ganador de una estadía para dos personas con todo pagado. ¡Felicidades!',
            from_email='no-reply@hotelpromo.com',
            recipient_list=[winner.email],
            fail_silently=False
        )

        return Response({"message": f"El ganador es {winner.full_name} con email {winner.email}"}, status=status.HTTP_200_OK)    
    