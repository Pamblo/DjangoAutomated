from django.urls import path
from . import views

app_name = 'empleado_app'

urlpatterns = [

    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-by-area/<nombre>/', views.ListByAreaEmpleados.as_view()),
    path('listar-by-job/<job>/', views.ListByTrabajoEmpleados.as_view()),
    path('listar-by-kword/', views.ListEmpleadosByKword.as_view()),
    path('listar-habilidades/', views.ListHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>', views.EmpleadoDetailView.as_view()),
    path('add-empleado/', views.EmpleadoCreateView.as_view()),
    path('success/', views.SuccesView.as_view(), name='correcto'),
    path('actualizar-empleado/<pk>', views.EmpleadoUpdateView.as_view(), name='Modificar_empleado'),
    path('borrar-empleado/<pk>', views.EmpleadoDeleteView.as_view(), name='Borrar')
]