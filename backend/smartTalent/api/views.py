from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from .models import (
    Convocatoria,Postulante,Academico,Laboral,Psicologico,Calificacion
)

from .serializers import(
    ConvocatoriaSerializer,PostulanteSerializerPOST,PostulanteSerializerGET ,AcademicoSerializerPOST,AcademicoSerializerGET,LaboralSerializerGET,LaboralSerializerPOST,PsicologicoSerializerGET,PsicologicoSerializerPOST,CalificacionSerializerGET,CalificacionSerializerPOST
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


class PostulanteView(APIView):

    def get(self,request):
        dataPostulante = Postulante.objects.all()
        serPostulante = PostulanteSerializerGET(dataPostulante,many=True)

        context = {
            'ok':True,
            'postulante':serPostulante.data
        }

        return Response(context)

    def post(self,request):
        serPostulante = PostulanteSerializerPOST(data=request.data)
        serPostulante.is_valid(raise_exception=True)
        serPostulante.save()

        context = {
            'ok':True,
            'content':serPostulante.data
        }
        return Response(context)

class AcademicoView(APIView):

    def get(self,request):
        dataAcademico = Academico.objects.all()
        serAcademico = AcademicoSerializerGET(dataAcademico,many=True)

        context = {
            'ok':True,
            'academco':serAcademico.data
        }

        return Response(context)

    def post(self,request):
        serAcademico = AcademicoSerializerPOST(data=request.data)
        serAcademico.is_valid(raise_exception=True)
        serAcademico.save()

        context = {
            'ok':True,
            'content':serAcademico.data
        }
        return Response(context)


class LaboralView(APIView):

    def get(self,request):
        dataLaboral = Laboral.objects.all()
        serLaboral = LaboralSerializerGET(dataLaboral,many=True)

        context = {
            'ok':True,
            'laboral':serLaboral.data
        }

        return Response(context)

    def post(self,request):
        serLaboral = LaboralSerializerPOST(data=request.data)
        serLaboral.is_valid(raise_exception=True)
        serLaboral.save()

        context = {
            'ok':True,
            'content':serLaboral.data
        }
        return Response(context)

class PsicologicoView(APIView):

    def get(self,request):
        dataPsicologico = Psicologico.objects.all()
        serPsicologico = PsicologicoSerializerGET(dataPsicologico,many=True)

        context = {
            'ok':True,
            'psicologico':serPsicologico.data
        }

        return Response(context)

    def post(self,request):
        serPsicologico = PsicologicoSerializerPOST(data=request.data)
        serPsicologico.is_valid(raise_exception=True)
        serPsicologico.save()

        context = {
            'ok':True,
            'content':serPsicologico.data
        }
        return Response(context)


class CalificacionView(APIView):

    def get(self,request):
        dataCalificacion = Calificacion.objects.all()
        serCalificacion = CalificacionSerializerGET(dataCalificacion,many=True)

        context = {
            'ok':True,
            'calificacion':serCalificacion.data
        }

        return Response(context)

    def post(self,request):
        serCalificacion = CalificacionSerializerPOST(data=request.data)
        serCalificacion.is_valid(raise_exception=True)
        serCalificacion.save()

        context = {
            'ok':True,
            'content':serCalificacion.data
        }
        return Response(context)