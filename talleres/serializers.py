from rest_framework import serializers
from .models import TipoTaller, Taller

class TipoTallerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTaller
        fields = ['id', 'nombre', 'descripcion', 'imagen']


class TallerSerializer(serializers.ModelSerializer):
    tipo_taller_nombre = serializers.CharField(source='tipo_taller.nombre', read_only=True)

    class Meta:
        model = Taller
        fields = ['id', 'tema', 'fecha', 'duracion', 'ponente', 'tipo_taller', 'tipo_taller_nombre']
