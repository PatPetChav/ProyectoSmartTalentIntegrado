from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from .models import (
    Convocatoria
)

from .serializers import(
    ConvocatoriaSerializer
)

class IndexView(APIView):

    def get(self,request):
        context = {
            'ok':True,
            'message':'el servidor de SmartTalent esta activo aqui!'
        }
        return Response(context)


class ConvocatoriaView(APIView):

    def get(self,request):
        dataConvocatoria = Convocatoria.objects.all()
        serConvocatoria = ConvocatoriaSerializer(dataConvocatoria,many=True)
       
        context = {
            'ok':True,
            'content':serConvocatoria.data
        }

        return Response(context)