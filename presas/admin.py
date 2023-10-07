from django.contrib import admin
from presas.models import *


class adminWorld(admin.ModelAdmin):
    model = WorldBorder
    list_display = ("name", "area", "pop2005")
    search_fields = ["name"]


admin.site.register(WorldBorder, adminWorld)
