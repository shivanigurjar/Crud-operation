from django.contrib import admin
from .models import your_model
# Register your models here.
@admin.register(your_model)
class firstAdmin(admin.ModelAdmin):
    list_display = ('id','First_name','Last_name','Password')
 