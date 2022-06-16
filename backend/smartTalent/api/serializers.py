from rest_framework import serializers

from .models import ( Convocatoria,Postulante,Academico,Laboral, Psicologico,Calificacion,Test);

class ConvocatoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convocatoria
        fields = '__all__'
    
    def to_representation(self, instance):
        representacion = super().to_representation(instance)
        representacion['convocatoria_photo'] = instance.convocatoria_photo.url
        return representacion

class PostulanteSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Postulante
        fields = ['postulante_id','postulante_nombre','postulante_apellido','postulante_dni','postulante_email','postulante_fecha_nacimiento','postulante_genero','postulante_pais','postulante_celular','postulante_departamento','postulante_provincia','postulante_direccion','fecha_postulacion','mes_postulacion','estado']

   
class PostulanteSerializerGET(serializers.ModelSerializer):
    class Meta:
        model = Postulante
        fields = '__all__'



class AcademicoSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Academico
        fields = ['calificacion_id','postulante_id','profesion','area_profesional','nivel_academico','centro_estudios','fecha_egreso','curso_adicional_1','curso_adicional_2','nivel_ingles']

class AcademicoSerializerGET(serializers.ModelSerializer):
    class Meta:
        model = Academico
        fields = '__all__'

class LaboralSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Laboral
        fields = ['laboral_id','postulante_id','nombre_empresa','ruc','telefono','direccion','cargo_desempenho','fecha_inicio','fecha_termino','descripcion_actividad','tiempo']
   
class LaboralSerializerGET(serializers.ModelSerializer):
    class Meta:
        model = Laboral
        fields = '__all__'
    
class PsicologicoSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Psicologico
        fields = ['psicologico_id','postulante_id','test_id','calificacion']
   
class PsicologicoSerializerGET(serializers.ModelSerializer):
    class Meta:
        model = Psicologico
        fields = '__all__'

class CalificacionSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = ['calificacion_id','postulante_id','convocatoria_id','calf_academica','calf_laboral','calf_psicologica','calf_asertividad','calf_autoestima','calf_comunicacion','calf_tomadecision','estado']
   
class CalificacionSerializerGET(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = '__all__'


class TestSerializerGET(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'
