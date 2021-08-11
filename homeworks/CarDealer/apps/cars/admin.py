from django.contrib import admin
from apps.cars.models import *

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'dealer',)
    autocomplete_fields = ('dealer', 'model', 'color')
    search_fields = ('model', 'dealer', 'price')


admin.site.register(Car, CarAdmin)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Property)
admin.site.register(CarProperty)
admin.site.register(Picture)
