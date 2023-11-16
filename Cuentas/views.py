from django.shortcuts import render
from .models import Cuenta
from Clientes.models import Cliente
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def listado(request):
        cuentas = Cuenta.objects.all()
        if request.user.is_superuser == 1:
                return render(request, "Cuentas/cuentas.html", {"cuentas":cuentas})
        else:
                return render(request, "Clientes/error.html", {"cuentas":""})

@login_required
def por_cliente(request, id_cliente):
        cliente = Cliente.objects.get(pk=id_cliente)
        cuentas = Cuenta.objects.filter(cliente_id__exact = id_cliente)
        if cliente.usuario_id == request.user.id:
                return render(request, "Cuentas/cuentas_cliente.html", {"cuentas":cuentas,
                                                                "cliente": cliente})
        else:
                return render(request, "Clientes/error.html", {"cuentas":""})
