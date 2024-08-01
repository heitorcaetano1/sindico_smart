from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.funcionarios.models import Funcionarios


@login_required
def index_view(request):

    user = request.user
    funcionarios = Funcionarios.objects.all()
    context = {
        'username': user.username,
        'funcionarios': funcionarios,
    }

    return render(request, 'index.html', context)
