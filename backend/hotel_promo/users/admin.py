from django.contrib import admin
from .models import Contestant

@admin.register(Contestant)
class ContestantAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'email_verified', 'phone')
    search_fields = ('email', 'full_name')
