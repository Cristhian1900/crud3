from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import TipoTaller, Taller
from .serializers import TipoTallerSerializer, TallerSerializer

class TipoTallerViewSet(viewsets.ModelViewSet):
    queryset = TipoTaller.objects.all()
    serializer_class = TipoTallerSerializer
    parser_classes = [MultiPartParser, FormParser]  


class TallerViewSet(viewsets.ModelViewSet):
    queryset = Taller.objects.all()
    serializer_class = TallerSerializer