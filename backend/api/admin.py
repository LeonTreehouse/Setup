from django.contrib import admin

from . import models

@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand']