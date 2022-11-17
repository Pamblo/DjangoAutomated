from django.db import models

# Create your models here.

class Departamento(models.Model):

    nombre = models.CharField('Nombre',max_length=30)
    nombre_corto = models.CharField('Nombre Corto', max_length=20)
    anulado = models.BooleanField('Anulado', default=False)


    def __str__(self):
        return str(self.nombre) + '-' + str(self.nombre_corto)


