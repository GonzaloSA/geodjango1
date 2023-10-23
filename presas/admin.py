from django.contrib import admin
from presas.models import *


class adminWorld(admin.ModelAdmin):
    model = WorldBorder
    list_display = ("name", "area", "pop2005")
    search_fields = ["name"]


class adminFugas(admin.ModelAdmin):
    model = HistoricoFugas
    list_display = ("alcaldia", "entidad")
    search_fields = ["alcaldia"]


admin.site.register(WorldBorder, adminWorld)
admin.site.register(HistoricoFugas, adminFugas)
