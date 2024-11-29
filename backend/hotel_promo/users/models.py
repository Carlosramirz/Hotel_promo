from django.db import models

# Create your models here.

class Contestant(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=9)
    email_verified = models.BooleanField(default=False)
    winner = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email