from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView
from .models import Inquilinos, Condominios
from .forms import InquilinoForm, DependentesForm, VeiculosForm, AnimaisForm


@method_decorator(login_required, name='dispatch')
class InquilinosCreateView(CreateView):
    model = Inquilinos
    form_class = InquilinoForm
    template_name = 'inquilino_form.html'
    success_url = 'inquilino_list.html'

    def form_valid(self, form):

        self.object = form.save(commit=False)
        logged_in_user = self.request.user
        self.object.condominio = Condominios.objects.filter(usuario=logged_in_user).first()


        dependentes_form = DependentesForm(self.request.POST)
        if dependentes_form.is_valid():
            dependentes = dependentes_form.save(commit=False)
            dependentes.inquilino = self.object
            dependentes.save()

        veiculos_form = VeiculosForm(self.request.POST)
        if veiculos_form.is_valid():
            veiculos = veiculos_form.save(commit=False)
            veiculos.save()
            self.object.veiculos.add(veiculos)

        animais_form = AnimaisForm(self.request.POST)
        if animais_form.is_valid():
            animais = animais_form.save(commit=False)
            animais.save()
            self.object.animais.add(animais)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dependentes_form'] = DependentesForm()
        context['veiculos_form'] = VeiculosForm()
        context['animais_form'] = AnimaisForm()
        return context


def excluir_inquilio(request, inquilino_id):
    inquilino = get_object_or_404(Inquilinos, id=inquilino_id)
    inquilino.delete()
    return redirect('inquilino_list')


class InquilinoListView(ListView):
    model = Inquilinos
    template_name = 'inquilinos_list.html'
    context_object_name = 'inquilinos'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.GET.get('search')
        if search_term:
            queryset = queryset.filter(name_icontains=search_term)

        return queryset


def detalhe_morador(request, id_inquilino):
    inquilino = get_object_or_404(Inquilinos, pk=id_inquilino)
    return render(request, 'morador.html', {'inquilino': inquilino})
