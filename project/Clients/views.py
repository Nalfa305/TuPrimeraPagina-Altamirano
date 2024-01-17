from django.shortcuts import redirect, render

from . import forms, models


def index(request):
    return render(request, "Clients/index.html")


def pais_list(request):
    paises = models.Pais.objects.all()
    context = {"paises": paises}
    return render(request, "Clients/pais_list.html", context)


def cliente_list(request):
    clientes = models.Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request, "Clients/cliente_list.html", context)


def cliente_create(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:cliente_list")
    else: #if request.method == "GET":
        form = forms.ClienteForm()
    return render(request, "Clients/cliente_create.html", {"form": form})