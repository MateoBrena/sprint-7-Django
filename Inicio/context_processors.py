from Clientes.models import Cliente

def cliente_processor(request):
    if request.user.is_authenticated or request.user.is_superuser == 1:
        cliente = Cliente.objects.filter(usuario_id__exact=request.user.id).first()
        return{"cliente":cliente}
    else:
        return{"cliente":""}