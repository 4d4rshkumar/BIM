from django.contrib import admin

# Register your models here.
from inventory.models import InventoryItems
admin.site.register(InventoryItems)
