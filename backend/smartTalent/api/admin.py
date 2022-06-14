from django.contrib import admin

# Register your models here.
from .models import Postulante,Empresa,Convocatoria

admin.site.register(Postulante)
admin.site.register(Empresa)
admin.site.register(Convocatoria)
