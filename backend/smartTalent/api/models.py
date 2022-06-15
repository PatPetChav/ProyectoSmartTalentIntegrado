from django.db import models
from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

class Postulante(models.Model):
    # genero
    MASCULINO = 'masculino'
    FEMENINO = 'femenino'

    GENERO_CHOICES = (
        (MASCULINO,'Masculino'),
        (FEMENINO,'Femenino')
    )

    # estado
    ACTIVO = 'activo'
    INACTIVO = 'inactivo'

    ESTADO_CHOICES = (
        (ACTIVO,'Activo'),
        (INACTIVO,'Inactivo')
    )

    postulante_id = models.AutoField(primary_key=True)
    postulante_nombre = models.CharField(max_length=100,verbose_name="Nombre Postulante")
    postulante_apellido = models.CharField(max_length=100,verbose_name="Apellido Postulante")
    postulante_dni = models.CharField(max_length=15,verbose_name="DNI")
    postulante_email = models.EmailField(verbose_name="Email")
    postulante_fecha_nacimiento = models.DateTimeField(null=True,verbose_name='Nacimiento')
    postulante_genero = models.CharField(max_length=15,default='masculino',choices=GENERO_CHOICES)
    postulante_pais = models.CharField(max_length=50,verbose_name="Pais Nacimiento")
    postulante_celular = models.CharField(max_length=15)
    postulante_departamento = models.CharField(max_length=50)
    postulante_provincia = models.CharField(max_length=50)
    postulante_direccion = models.CharField(max_length=100)
    fecha_postulacion = models.DateTimeField(null=True,verbose_name='Fecha Postulación')
    mes_postulacion = models.IntegerField(default=1)
    estado = models.CharField(max_length=15,default='activo',choices=ESTADO_CHOICES)

    def __str__(self):
        return self.postulante_nombre


class Academico(models.Model):
     # nivel academico
    SECUNDARIA = 'secundaria'
    TECNICO = 'tecnico'
    UNIVERSITARIO = 'universitario'
    TITULADO = 'titulado'
    MAESTRIA = 'maestria'
    DOCTORADO = 'doctorado'

    NIVEL_CHOICES = (
        (SECUNDARIA,'Secundaria'),
        (TECNICO,'Técnico'),
        (UNIVERSITARIO,'Universitario'),
        (TITULADO,'Titulado'),
        (MAESTRIA,'Maestría'),
        (DOCTORADO,'Doctorado')
    )

      # ingles
    NINGUNO = 'ninguno'
    BASICO = 'basico'
    INTERMEDIO = 'intermedio'
    AVANZADO = 'avanzado'
    NATIVO = 'nativo'    

    INGLES_CHOICES = (
        (NINGUNO,'Ninguno'),
        (BASICO,'Básico'),
        (INTERMEDIO,'Intermedio'),
        (AVANZADO,'Avanzado'),
        (NATIVO,'Nativo')
    )

    calificacion_id=models.AutoField(primary_key=True)
    postulante_id = models.ForeignKey(Postulante,on_delete=models.RESTRICT)
    profesion = models.CharField(max_length=100,verbose_name="Profesion")
    area_profesional = models.CharField(max_length=15)
    nivel_academico = models.CharField(max_length=15,default='universitario',choices=NIVEL_CHOICES)
    centro_estudios = models.CharField(max_length=50,verbose_name="Centro de Estudios")
    fecha_egreso = models.DateTimeField(null=True,verbose_name='Fecha de egreso')
    curso_adicional_1 = models.CharField(max_length=100,verbose_name="Curso Adicional 1")
    curso_adicional_2 = models.CharField(max_length=100,verbose_name="Curso Adicional 2")
    nivel_ingles = models.CharField(max_length=15,default='basico',choices=INGLES_CHOICES)
    
    def __str__(self):
        return self.profesion

class Laboral(models.Model):

      # estado
    DE0A1ANHO = 'De 0 a 1 anho'
    DE1A2ANHOS = 'De 1 a 2 anhos'
    DE2A3ANHOS = 'De 2 a 3 anhos'
    DE3AMAS = '3 anhos a mas'

    TIEMPO_CHOICES = (
        (DE0A1ANHO,'De 0 a 1 anho'),
        (DE1A2ANHOS,'De 1 a 2 anhos'),
        (DE2A3ANHOS,'De 2 a 3 anhos'),
        (DE3AMAS,'3 anhos a mas')
    )

    laboral_id=models.AutoField(primary_key=True)
    postulante_id = models.ForeignKey(Postulante,on_delete=models.RESTRICT)
    nombre_empresa = models.CharField(max_length=100,verbose_name="Nombre Empresa")
    ruc = models.CharField(max_length=25,verbose_name="RUC")
    telefono = models.CharField(max_length=15,verbose_name="Teléfono de Empresa")
    direccion = models.CharField(max_length=100,verbose_name="Dirección de Empresa")
    cargo_desempenho = models.CharField(max_length=100,verbose_name="Cargo")
    fecha_inicio = models.DateTimeField(null=True,verbose_name='Fecha inicio')
    fecha_termino = models.DateTimeField(null=True,verbose_name='Fecha termino')
    descripcion_actividad = models.CharField(max_length=500,verbose_name="Descripción de Actividad")
    tiempo = models.CharField(max_length=25,default='0',choices=TIEMPO_CHOICES)

    def __str__(self):
        return self.cargo_desempenho    

class Test(models.Model):
    test_id=models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=100,verbose_name="Pregunta")
    nunca = models.IntegerField(default=0)
    rara_vez = models.IntegerField(default=0)
    a_veces = models.IntegerField(default=0)
    a_menudo = models.IntegerField(default=0)
    siempre = models.IntegerField(default=0)

    def __str__(self):
        return self.pregunta

class Psicologico(models.Model):
    psicologico_id=models.AutoField(primary_key=True)
    postulante_id = models.ForeignKey(Postulante,on_delete=models.RESTRICT)
    test_id = models.ForeignKey(Test,on_delete=models.RESTRICT)
    calificacion = models.IntegerField(default=0)

    def __str__(self):
        return self.calificacion

class Empresa(models.Model):
    empresa_convoca_id=models.AutoField(primary_key=True)
    nombre_empresa_convoca = models.CharField(max_length=100,verbose_name="Nombre Empresa")
    usuario = models.OneToOneField(User,on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.nombre_empresa_convoca

class Convocatoria(models.Model):
    # estado
    ACTIVO = 'activo'
    INACTIVO = 'inactivo'

    ESTADO_CHOICES = (
        (ACTIVO,'Activo'),
        (INACTIVO,'Inactivo')
    )

    convocatoria_id=models.AutoField(primary_key=True)
    empresa_convoca_id = models.ForeignKey(Empresa,on_delete=models.RESTRICT)
    convocatoria_nombre = models.CharField(max_length=100,verbose_name="Nombre Convocatoria")
    nombre_entidad = models.CharField(max_length=50,verbose_name="Entidad")
    convocatoria_photo = CloudinaryField('image',default='')
    convocatoria_descripcion = models.CharField(null=True,max_length=1000,verbose_name="descripcion Convocatoria")
    # convocatoria_photo = models.ImageField(upload_to='photos',blank=True)

    fecha_inicio = models.DateTimeField(null=True,verbose_name='Fecha inicio')
    fecha_termino = models.DateTimeField(null=True,verbose_name='Fecha termino')
    numero_vacantes = models.IntegerField(default=1)
    remuneracion = models.DecimalField(max_digits=9,decimal_places=2)
    estado = models.CharField(max_length=15,default='activo',choices=ESTADO_CHOICES)
    
    def __str__(self):
        return self.convocatoria_nombre

class Calificacion(models.Model):

    # estado
    ACTIVO = 'activo'
    INACTIVO = 'inactivo'

    ESTADO_CHOICES = (
        (ACTIVO,'Activo'),
        (INACTIVO,'Inactivo')
    )

    calificacion_id=models.AutoField(primary_key=True)
    postulante_id = models.ForeignKey(Postulante,on_delete=models.RESTRICT)
    convocatoria_id = models.ForeignKey(Convocatoria,on_delete=models.RESTRICT)
    calf_academica = models.DecimalField(max_digits=9,decimal_places=2)
    calf_laboral = models.DecimalField(max_digits=9,decimal_places=2)
    calf_psicologica = models.DecimalField(max_digits=9,decimal_places=2)
    calf_asertividad = models.DecimalField(max_digits=9,decimal_places=2)
    calf_autoestima = models.DecimalField(max_digits=9,decimal_places=2)
    calf_comunicacion = models.DecimalField(max_digits=9,decimal_places=2)
    calf_tomadecision = models.DecimalField(max_digits=9,decimal_places=2)
    estado = models.CharField(max_length=15,default='activo',choices=ESTADO_CHOICES)

    def __str__(self):
        return self.calf_academica
