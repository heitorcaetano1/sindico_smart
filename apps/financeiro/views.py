from xhtml2pdf import pisa
from django.core.mail import EmailMessage
from reportlab.pdfgen import canvas

from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template.loader import get_template

from .models import Conta
import csv
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
import io
from .forms import BoletoForm
from .forms import ContaForm, FluxiCaixaForm
from .models import Boleto


def check_funcionario_role(user):
    return user.funcionario.is_administracao_or_contabilidade()


@login_required
@user_passes_test(check_funcionario_role)
def financeiro(request):
    if request.method == 'POST':
        conta_form = ContaForm(request.POST)
        fluxo_form = FluxiCaixaForm(request.POST)
        if conta_form.is_valid() and fluxo_form.is_valid():
            conta_form.save()
            fluxo_form.save()
            return redirect('financeiro')

    else:
        conta_form = ContaForm()
        fluxo_form = FluxiCaixaForm()
    return render(request, 'templates/financeiro.html',
                  {'conat_form': conta_form, 'fluxo_form': fluxo_form})


def gerar_relatorio_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Conten-Disposition'] = 'attachment; filename="relatorio_financeiro.csv"'

    writer = csv.writer(response)
    writer.writerow(['Descrição', 'Valor', 'Data Vencimento', 'Tipo', 'Status'])

    contas = Conta.objects.all()
    for conta in contas:
        writer.writerow([conta.descricao, conta.valor, conta.data_vencimento,
                         conta.tipo, conta.status])

    return response


def gerar_relatorio_pdf(request):
    contas = Conta.objects.all()
    template_path = 'finaceiro/relatorio_pdf.html'
    context = {'contas': contas}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_financeiro.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Ocorreu um erro ao gerar o relatório PDF.', status=400)
    return response


def gerar_boleto_com_codigo_barras(request, boleto_id):
    boleto = get_object_or_404(Boleto, id=boleto_id)
    if not boleto.codigo_barras:
        boleto.gerar_codigo_barras()
        boleto.save()


@login_required
def criar_boleto(request):
    if request.method == 'POST':
        form = BoletoForm(request.POST)
        if form.is_valid():
            boleto = form.save()
            return redirect('enviar_boleto', boleto_id=boleto)
    else:
        form = BoletoForm()
    return render(request, 'financeiro/criar_boleto.html', {'form': form})


@login_required
def enviar_boleto(request, boleto_id):
    boleto = Boleto.objects.get(id=boleto_id)
    pdf = gerar_boleto_pdf(boleto)

    if 'enviar_email' in request.POST:
        enviar_boleto_email(boleto, pdf, request.POST['email_destinatario'])
    elif 'enviar_whatsapp' in request.POST:
        pass
    return render(request, 'financeiro/enviar_boleto.html', {'boleto': boleto})


def gerar_boleto_pdf(boleto):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 750, f"Boleto: {boleto.descricao}")
    p.drawString(100, 750, f'Valor: {boleto.valor}')
    p.drawString(100, 750, f'Vencimento: {boleto.data_vencimanto}')
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer


def enviar_boleto_email(boleto, pdf, email_destinatrio):
    email = EmailMessage(
        'Seu  Boleto do Condomínio',
        'Segue em anexo o boleto para pagamento.',
        settings.EMAIL_HOST_USER,
        [email_destinatrio]
    )
    email.attach(f'boleto_{boleto.id}.pdf', pdf.getvalue(), 'application/pdf')
    email.send()
