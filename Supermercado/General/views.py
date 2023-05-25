from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from .models import *
from .forms import *

# Create your views here.

class ObtenerCargos(View):
    def get(self, request):
        cargos = Cargo.objects.all()

        return render(request, 'cargos/listar_cargos.html',{'cargos':cargos})


class AgregarCargo(View):
    def get(self, request):
        form = AddcargoForm()

        return render(request, 'cargos/agregar_cargo.html', {'form': form})

    def post(self, request):
        form = AddcargoForm(request.POST)

        if(form.is_valid()):
            obj = Cargo()
            obj.name = form.cleaned_data['name']
            obj.save()

            return HttpResponseRedirect(reverse('listar_cargos'))


class ActualizarCargo(View):
    def get(self, request, uuid):
        obj = Cargo.objects.get(uuid=uuid)
        form = UpdateCargoForm(instance=obj)

        return render(request, 'cargos/agregar_cargo.html', {'form': form})
    
    def post(self, request, uuid):
        obj = Cargo.objects.get(uuid=uuid)
        form = UpdateCargoForm(request.POST, instance=obj)

        if (form.is_valid()):
            obj = form.save(commit=False)
            obj.save()

        return HttpResponseRedirect(reverse('listar_cargos'))


class ObtenerClientes(View):
    def get(self, request):
        clientes = Cliente.objects.all()

        return render(request, 'clientes/listar_clientes.html',{'clientes':clientes})
    
class AgregarClientes(View):
    def get(self, request):
        form = AddClienteForm()

        return render(request, 'clientes/agregar_clientes.html', {'form': form})

    def post(self, request):
        form = AddClienteForm(request.POST)

        if(form.is_valid()):
            obj = Cliente()
            obj.person = form.cleaned_data['person']
            obj.address = form.cleaned_data['address']
            obj.phone = form.cleaned_data['phone']
            obj.save()

            return HttpResponseRedirect(reverse('listar_clientes'))
        else:
            print(form.errors)

class ActualizarCliente(View):
    def get(self, request, uuid):
        obj = Cliente.objects.get(uuid=uuid)
        form = UpdateClienteForm(instance=obj)
    
        return render(request, 'clientes/actualizar_clientes.html', {'form': form})



class ObtenerUsuarios(View):
    def get(self, request):
        usuarios = Usuario.objects.all()

        return render(request, 'usuarios/listar_usuarios.html',{'usuarios':usuarios})
