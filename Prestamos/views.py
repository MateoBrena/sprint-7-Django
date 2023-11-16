from django.shortcuts import render, redirect
from .forms import FormPrestamo
from .models import Prestamo
from Clientes.models import Cliente
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def prestamo(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    if cliente.usuario_id == request.user.id:
        form_prestamo = FormPrestamo
        

        if request.method == "POST":
            form_prestamo = form_prestamo(data=request.POST)

            if form_prestamo.is_valid():
                tipoRecibido = request.POST.get('tipo','')
                fechaRecibida =  request.POST.get('fecha','')

                prestamo = Prestamo( tipo = tipoRecibido, fecha = fechaRecibida) #monto = montoYaDefinido, cliente = clienteYaDefinido)
                prestamo.save()

        return render(request, "Prestamos/prestamo.html", {"form":form_prestamo,
                                                       "cliente":cliente})
    else:
        return render(request, "Clientes/error.html", {"forms":""})