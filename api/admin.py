from django.contrib import admin
from .models import Item

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('sensor_id', 'e_data', 'created',)

admin.site.register(Item, ItemAdmin)
