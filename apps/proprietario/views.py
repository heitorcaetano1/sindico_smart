from django.shortcuts import render, get_object_or_404, redirect
from .models import Proprietario
from .forms import ProprietarioForm


def lista_proprietario(request):
    proprietario = Proprietario.objects.all()
    return render(request, 'proprietarios.html',
                  {'proprietario': proprietario})


def detalhes_proprietario(request, proprietario_id):
    proprietario = get_object_or_404(Proprietario, id=proprietario_id)
    if request.method == 'POST':
        form = ProprietarioForm(request.POST, instance=proprietario)
        if form.is_valid():
            form.save()
            return redirect('lista_proprietario')
    else:
        form = ProprietarioForm(instance=proprietario)

    return render(request, 'edt_proprietario.html', {'form': form, 'proprietario': proprietario})


def registro_proprietario(request):
    if request.method == 'POST':
        form = ProprietarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('proprietarios')
    else:
        form = ProprietarioForm()

    return render(request, 'proprietario_form.html', {'form': form})


def edit_proprietario(request, proprietario_id):
    proprietario = get_object_or_404(Proprietario, id=proprietario_id)
    if request.method == 'POST':
        form = ProprietarioForm(request.POST, instance=proprietario)
        if form.is_valid():
            form.save()
            return redirect('lista_proprietario')
    else:
        form = ProprietarioForm(instance=proprietario)

    return render(request, 'edit_proprietario.html', {'form': form, 'proprietario': proprietario})

