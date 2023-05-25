from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .models import *
from .forms import *

# Create your views here.

class ObtenerFacturas(View):
    def get(self, request):
        facturas = Factura.objects.all()

        return render(request, 'facturas/listar_facturas.html', {'facturas':facturas})
    
class AgregarFacturas(View):
  def get(self, request):
        form = AddFacturaForm()

        return render(request, 'facturas/agregar_factura.html', {'form': form})
       

  def post(self, request):
        form = AddFacturaForm(request.POST)

        if(form.is_valid()):
            obj = Factura()
            obj.client = form.cleaned_data['uuid']
            obj.rtn = form.cleaned_data['rtn']
            obj.save()

            return HttpResponseRedirect(reverse('listar_facturas'))
