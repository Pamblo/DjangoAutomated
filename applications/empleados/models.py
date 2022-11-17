from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.
class Habilidades(models.Model):

    """Modelo para habilidades del empleado"""
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:

        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleado'

    def __str__(self):
        return str(self.habilidad)
class Empleado(models.Model):

    """Modelo para tabla empleado"""
    trabajos = (
        ('0','Contable'),
        ('1','Administrador'),
        ('2', 'Economista'),
        ('3', 'OTRO')
    )

    nombre = models.CharField('Nombre', max_length=30)
    apellidos = models.CharField('Apellidos', max_length=60)
    trabajo = models.CharField('Trabajo', max_length=1, choices=(trabajos))
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:

        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['nombre','apellidos']
        unique_together = ('nombre','apellidos')

    def __str__(self):

        return str(self.nombre) + '-' + str(self.apellidos)

