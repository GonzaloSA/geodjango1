from django.core.management.base import BaseCommand
from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from presas.models import WorldBorder, HistoricoFugas


class Command(BaseCommand):
    def loadWorld(self):
        world_mapping = {
            "fips": "FIPS",
            "iso2": "ISO2",
            "iso3": "ISO3",
            "un": "UN",
            "name": "NAME",
            "area": "AREA",
            "pop2005": "POP2005",
            "region": "REGION",
            "subregion": "SUBREGION",
            "lon": "LON",
            "lat": "LAT",
            "mpoly": "MULTIPOLYGON",
        }
        world_shp = (
            Path(__file__).resolve().parent / "data" / "TM_WORLD_BORDERS-0.3.shp"
        )
        lm = LayerMapping(WorldBorder, world_shp, world_mapping, transform=False)
        lm.save(strict=True, verbose=True)

    def loadFugas(self):
        fugas_mapping = {
            "anio": "ANO",
            "alcaldia": "ALCALDIA",
            "diam_pulg": "DIAM_PULG",
            "entidad": "ENTIDAD",
            "minicipio": "MUNICIPIO",
            "nombre": "NOMBRE",
            "cp": "CP",
            "otros_cp": "OTROS_CP",
            "nomvial": "NOMVIAL",
            "mpoint": "MULTIPOINT",
        }
        fugas_shp = Path(__file__).resolve().parent / "data" / "fugas.shp"
        lm = LayerMapping(HistoricoFugas, fugas_shp, fugas_mapping, transform=False)
        lm.save(strict=True, verbose=True)

    def handle(self, *args, **options):
        self.loadFugas()
