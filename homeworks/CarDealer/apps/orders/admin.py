from django.contrib import admin
from apps.orders.models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = ('car', 'status', 'id')
    list_filter = ('car', 'status', 'id')
    search_fields = ('car', 'status', 'id')

admin.site.register(Order, OrderAdmin)
