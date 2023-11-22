from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormPrestamo
from .models import Prestamo
from Clientes.models import Cliente
from Cuentas.models import Cuenta
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def prestamo(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    cuenta = Cuenta.objects.filter(cliente_id__exact = cliente_id, tipo_id__exact = 1).first()
    if cliente.usuario_id == request.user.id:
        
        initial_dict = {
            "nombre": cliente.name,
            "apellido": cliente.surname,
            "dni": cliente.dni
        }

        form_prestamo = FormPrestamo(initial = initial_dict)
        

        if request.method == "POST":
            form_prestamo = FormPrestamo(data=request.POST)

            if form_prestamo.is_valid() and cuenta:

                tipoRecibido = request.POST.get('tipo','')
                fechaRecibida =  request.POST.get('fecha','')
                montoRecibido =  request.POST.get('monto','')

                if cliente.tipo_id == 1 and int(montoRecibido) <= 100000:
                    prestamo = Prestamo( tipo = tipoRecibido, fecha = fechaRecibida, monto = montoRecibido, cliente_id = cliente.id)
                    prestamo.save()
                    cuenta.balance = cuenta.balance + int(montoRecibido)
                    cuenta.save()
                    messages.success(request, 'Préstamo otorgado, verificar en "Mis préstamos", el saldo en su cuenta '+ cuenta.iban +' ha sido actualizado')
                elif cliente.tipo_id == 2 and int(montoRecibido) <= 300000:
                    prestamo = Prestamo( tipo = tipoRecibido, fecha = fechaRecibida, monto = montoRecibido, cliente_id = cliente.id)
                    prestamo.save()
                    cuenta.balance = cuenta.balance + int(montoRecibido)
                    cuenta.save()
                    messages.success(request, 'Préstamo otorgado, verificar en "Mis préstamos", el saldo en su cuenta '+ cuenta.iban +' ha sido actualizado')
                elif cliente.tipo_id == 3 and int(montoRecibido) <= 500000:
                    prestamo = Prestamo( tipo = tipoRecibido, fecha = fechaRecibida, monto = montoRecibido, cliente_id = cliente.id)
                    prestamo.save()
                    cuenta.balance = cuenta.balance + int(montoRecibido)
                    cuenta.save()
                    messages.success(request, 'Préstamo otorgado, verificar en "Mis préstamos", el saldo en su cuenta '+ cuenta.iban +' ha sido actualizado')
                else:
                     messages.error(request, "Error: Préstamo rechazado. Monto máximo de cliente "+ str(cliente.tipo) + " superado")
            else:
                 messages.error(request, "Error: el cliente debe poseer una caja de ahorro en pesos para solicitar un préstamo")

        return render(request, "Prestamos/prestamo.html", {"form":form_prestamo,
                                                       "cliente":cliente,
                                                       "cuenta":cuenta})
    else:
        return render(request, "Clientes/error.html", {"forms":""})

@login_required    
def por_cliente(request, cliente_id):
        cliente = Cliente.objects.get(pk=cliente_id)
        prestamos = Prestamo.objects.filter(cliente_id__exact = cliente_id)
        if cliente.usuario_id == request.user.id:
             return render(request, "Prestamos/prestamos_cliente.html", {"prestamos":prestamos,
                                                       "cliente":cliente})