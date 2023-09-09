from django.contrib import admin
from .models import Utilizator

# Register your models here.

class UtilizatorAdmin(admin.ModelAdmin):
   list_display=("username","nr_matricol","email","password")

admin.site.register(Utilizator,UtilizatorAdmin)