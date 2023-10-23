from django.shortcuts import render
from presas.models import *
import json
from django.db.models import Count
from django.http import JsonResponse


def map_view(request):
    mexico = WorldBorder.objects.all()
    # mex = mexico.geojson
    # estados = []
    # estados.append(mexico)
    # estados_geojson = serialize("geojson", estados)
    # print(mex)
    context = {"poligonos": mexico}
    return render(request, "map/map.html", context)


def mapa_fugas(request):
    # fugas = HistoricoFugas.objects.all()
    # data = serialize("json", fugas)
    # historico_fugas_list = [entry["fields"] for entry in json.loads(data)]
    # context = {"fugas": historico_fugas_list}
    # return render(request, "map/fugas.html", context)
    # data = HistoricoFugas.objects.values("anio", "diam_pulg").annotate(
    #     total=Count("id")
    # )
    # return render(request, "map/fugas.html", {"data": data})
    alcaldias = HistoricoFugas.objects.values("alcaldia").distinct()
    return render(request, "map/fugas.html", {"alcaldias": alcaldias})


def obtener_datos_fugas(request):
    alcaldia_seleccionada = request.GET.get("alcaldia", None)

    if alcaldia_seleccionada:
        datos_fugas = HistoricoFugas.objects.filter(
            alcaldia=alcaldia_seleccionada
        ).values()
        print(list(datos_fugas))
        return JsonResponse({"datos_fugas": list(datos_fugas)})

    return JsonResponse({"error": "No se especificó una alcaldía válida"})
