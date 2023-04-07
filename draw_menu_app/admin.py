from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MenuNode)
class MenuNodeAdmin(admin.ModelAdmin):
    pass
