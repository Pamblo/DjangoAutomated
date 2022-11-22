from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
from .models import Empleado



class ListAllEmpleados(ListView):
    """Petición basica sin nada más que solicitar al servidor toda la información y mostrarla haciendo petición en el HTML
    Aquí lo importante está en que si no defiines el context_object_name puedes llamarlo desde HTML como object_list"""

    template_name = 'empleados/list_all.html'
    paginate_by = 4
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

class ListByTrabajoEmpleados(ListView):

    """Lista empleados de un tipo de trabajo donde se recoge la información escribiendo en la URL la petición. Desde la URL indicas con <pk> o <Cualquier palabra> dependiendo si quieres bsucar por ID o por palabra."""
    template_name = 'empleados/list_by_job.html'


    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        job = self.kwargs['job']
        lista = Empleado.objects.filter(
        trabajo=job
        )
        return lista

class ListEmpleadosByKword(ListView):

    """Lista empleados de un area que recoge la petición por parte del usuario en un Field de HTML. Generamos en el HTML un FORM GET y un botón de Buscar. Con el ID del form lo pasamos en request.GET.get
    y ya puedes filtrar en la base de datos EMPLEADO por palabra clave. Una vez recibida la lista la puedes mostrar donde quieras"""
    template_name = 'empleados/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')

        lista = Empleado.objects.filter(
            nombre=palabra_clave
        )
        print('lista resultado:', lista)
        return lista

class ListHabilidadesEmpleado(ListView):
    """ListView genera listas dentro de un HTML. Necesita de un template name para saber a que HTML apuntar y un context object para poder llamar a la lista desde HTML
    En este caso recogemos la información indicando el ID desde programación... pero no lo indica el usuario"""

    template_name = 'empleados/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=3)
        print(empleado.habilidades.all())
        return empleado.habilidades.all()

class EmpleadoDetailView(DetailView):
    """Detail view te permite redireccionarte a otra página HTML, puede ser para ver info de base de datos o simplemente redireccionar a otra URL como un botón de ver más información..."""

    model = Empleado
    template_name = "empleados/detail_empleado.html"

class SuccesView(TemplateView):
    template_name = 'empleados/success.html'


class EmpleadoCreateView(CreateView):
    """Neceista estos 4 campos, el model es la base de datos donde va a ser añadido
    el template name donde está el HTML
    Fields son las casillas que me ahorro en editar en HTML. luego en el forms con .as_p hago las casillas en parrafos
    success_url es donde va a redirigirte al enviar lso datos. Sino peta error al darle enviar"""

    model = Empleado
    template_name = 'empleados/add.html'
    fields = ['nombre', 'apellidos', 'trabajo', 'departamento', 'habilidades', 'hoja_vida']
    success_url = reverse_lazy('empleado_app:correcto')

    def form_valid(self, form):
        empleado = form.save()
        empleado.full_name = empleado.nombre + ' ' + empleado.apellidos
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleados/update.html"
    fields = ['nombre', 'apellidos', 'trabajo', 'departamento', 'habilidades']
    success_url = reverse_lazy('empleado_app:correcto')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleados/delete.html"
    success_url = reverse_lazy('empleado_app:correcto')

