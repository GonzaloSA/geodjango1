from django.shortcuts import render
from django.core.serializers import serialize
from presas.models import *
import json


def map_view(request):
    mexico = WorldBorder.objects.all()
    # mex = mexico.geojson
    # estados = []
    # estados.append(mexico)
    # estados_geojson = serialize("geojson", estados)
    # print(mex)
    context = {"poligonos": mexico}
    return render(request, "map/map.html", context)
