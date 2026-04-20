from django.shortcuts import render
from .models import Treino
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


"""dashboard
listar_treinos
detalhe_treino
editar_treino"""


@login_required
def listar_treinos(request):

    treinos = Treino.objects.filter(user=request.user)

    return render(request, 'treinos/listar.html', {
        'treinos': treinos
    })


@login_required
def detalhe_treino(request, pk):

    treino = get_object_or_404(
        Treino,
        id=pk,
        user=request.user
    )

    return render(request, 'treinos/detalhe.html', {
        'treino': treino
    })


def editar_treino(request, pk):
    treino = Treino.objects.get(id=pk)

    if request.method == 'POST':
        treino.title = request.POST['title']
        treino.description = request.POST['description']
        treino.save()

    return render(request, 'editar_treino.html', {'treino': treino})
