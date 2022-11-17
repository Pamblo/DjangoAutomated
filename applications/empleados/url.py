from django.urls import path
from . import views

urlpatterns = [

    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-by-area/<nombre>/', views.ListByAreaEmpleados.as_view())
]