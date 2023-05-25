from django.urls import path
from .views import *

urlpatterns = [
    path('cargos/', ObtenerCargos.as_view(), name='listar_cargos'),
    path('cargos/agregar', AgregarCargo.as_view(), name='agregar_cargos'),
    path('cargos/<uuid:uuid>/actualizar',ActualizarCargo.as_view(), name='actualizar_cargo'),
    path('clientes/', ObtenerClientes.as_view(), name='listar_clientes'),
    path('clientes/agregar', AgregarClientes.as_view(), name='agregar_clientes'),
    path('clientes/<uuid:uuid>/actualizar', ActualizarCliente.as_view(), name='actualizar_clientes'),
    path('usuarios/', ObtenerUsuarios.as_view(), name='listar_usuarios'),
]