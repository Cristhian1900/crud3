from django.db import models

class TipoTaller(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='tipo_talleres/', null=True, blank=True)  
    def __str__(self):
        return self.nombre


class Taller(models.Model):
    tema = models.CharField(max_length=100)
    fecha = models.DateField()
    duracion = models.CharField(max_length=50)
    ponente = models.CharField(max_length=100)
    tipo_taller = models.ForeignKey(TipoTaller, on_delete=models.CASCADE, related_name="talleres")

    def __str__(self):
        return self.tema
