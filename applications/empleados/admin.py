from django.contrib import admin
from .models import Empleado
from .models import Habilidades
# Register your models here.


admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'apellidos',
        'trabajo',
        'departamento'
    )
    search_fields = (
        'nombre',
        'apellidos',
    )
    list_filter = ('departamento','trabajo',)
    filter_horizontal = 'habilidades',


admin.site.register(Empleado,EmpleadoAdmin)