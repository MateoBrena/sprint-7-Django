from django.shortcuts import render
from .models import Tarjeta
from Clientes.models import Cliente
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def listado(request):
        tarjetas = Tarjeta.objects.all()
        if request.user.is_superuser == 1:
                return render(request, "Tarjetas/tarjetas.html", {"tarjetas":tarjetas})
        else:
                return render(request, "Clientes/error.html", {"tarjetas":""})

@login_required
def por_cliente(request, id_cliente):
        cliente = Cliente.objects.get(pk=id_cliente)
        tarjetas = Tarjeta.objects.filter(cliente_id__exact = id_cliente)
        if cliente.usuario_id == request.user.id:
                return render(request, "Tarjetas/tarjetas_cliente.html", {"tarjetas":tarjetas,
                                                                "cliente": cliente})
        else:
                return render(request, "Clientes/error.html", {"tarjetas":""})
                
