from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Empleado
from applications.departamento.models import Departamento


class ListAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    model = Empleado

class ListByAreaEmpleados(ListView):

    """Lista empleados de un area"""
    template_name = 'empleados/list_by_area.html'


    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        area = self.kwargs['nombre']
        lista = Empleado.objects.filter(
        departamento__nombre=area
    )
        return lista
