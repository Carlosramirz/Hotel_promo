from django.urls import path
from .views import RegisterContestant, VerifyEmail, AdminLogin, GenerateWinner

urlpatterns = [
    path('register/', RegisterContestant.as_view(), name='register'),
    path('verify-email/', VerifyEmail.as_view(), name='verify-email'),
    path('admin-login/', AdminLogin.as_view(), name='admin-login'),
    path('generate-winner/', GenerateWinner.as_view(), name='generate-winner'),
]