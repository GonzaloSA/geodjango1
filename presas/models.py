from django.contrib.gis.db import models


class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField("Population 2005")
    fips = models.CharField("FIPS Code", max_length=2, null=True)
    iso2 = models.CharField("2 Digit ISO", max_length=2)
    iso3 = models.CharField("3 Digit ISO", max_length=3)
    un = models.IntegerField("United Nations Code")
    region = models.IntegerField("Region Code")
    subregion = models.IntegerField("Sub-Region Code")
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    @property
    def coordenadas_list(self):
        return [[point.x, point.y] for point in self.mpoly]

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


class HistoricoFugas(models.Model):
    anio = models.IntegerField()
    alcaldia = models.CharField(max_length=255)
    diam_pulg = models.IntegerField()
    entidad = models.IntegerField()
    minicipio = models.IntegerField()
    nombre = models.CharField(max_length=255)
    cp = models.IntegerField()
    otros_cp = models.CharField(max_length=255, null=True, blank=True)
    nomvial = models.CharField(max_length=255)
    mpoint = models.MultiPointField()

    @property
    def coordenadas_list(self):
        return [[point.x, point.y] for point in self.mpoint]

    # Returns the string representation of the model.
    def __str__(self):
        return self.nombre
