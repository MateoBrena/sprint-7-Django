from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import createUserForm, ClienteForm
from .models import Cliente

# Create your views here.
@login_required
def listado(request):
        clientes = Cliente.objects.all()
        if request.user.is_superuser == 1:
                return render(request, "Clientes/clientes.html", {"clientes":clientes})
        else:
              return render(request, "Clientes/error.html", {"clientes":""})

@login_required
def detalle(request, cliente_id):
        cliente = Cliente.objects.get(pk=cliente_id)
        if cliente.usuario_id == request.user.id:
                return render(request, "Clientes/cliente_detail.html", {"cliente":cliente})
        else:
              return render(request, "Clientes/error.html", {"cliente":""})
        
        
def register(request):
    form = createUserForm
    cliente_form = ClienteForm

    if request.method == 'POST':
        form = createUserForm(request.POST)
        cliente_form = ClienteForm(request.POST)

        if form.is_valid() and cliente_form.is_valid():
            user = form.save()

            cliente = cliente_form.save(commit=False)
            cliente.usuario = user

            cliente.save()

            messages.success(request, 'Cuenta creada exitosamente')

            return redirect('login')

    context = {'form': form, 'cliente_form': cliente_form}
    return render(request, 'Clientes/register.html', context)
