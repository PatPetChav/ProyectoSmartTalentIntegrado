from rest_framework import serializers

from .models import ( Convocatoria)

class ConvocatoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convocatoria
        fields = '__all__'
    
    def to_representation(self, instance):
        representacion = super().to_representation(instance)
        representacion['convocatoria_photo'] = instance.convocatoria_photo.url
        return representacion