from django.contrib import admin
from menu.models import Coffe
# Register your models here.
@admin.register(Coffe)
class CoffeAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']