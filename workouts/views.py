from django.shortcuts import render, redirect
from .models import Treino, TreinoExercicio
from .forms import TreinoForm, TreinoExercicioForm
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

    if request.user.role == 'teacher':
        treinos = Treino.objects.filter(
            teacher=request.user).order_by('-created')
    else:
        treinos = Treino.objects.filter(student=request.user).order_by('day')

    return render(request, 'workouts/listar_treinos.html', {'treinos': treinos})
# Criar treino (professor)


@login_required
def treino_create(request):
    if request.method == 'POST':
        form = TreinoForm(request.POST)

        if form.is_valid():
            treino = form.save(commit=False)
            treino.teacher = request.user
            treino.save()
            return redirect('workouts:treino_detalhes', pk=treino.pk)
    else:
        form = TreinoForm()
    context = {'form': form}
    return render(request, 'workouts/treino_form.html', context)


@login_required
def treino_detalhes(request, pk):
    treino = get_object_or_404(Treino, pk=pk)
    exercicios = TreinoExercicio.objects.filter(
        treino=treino).order_by('order')

    if request.method == 'POST':
        form = TreinoExercicioForm(request.POST)

        if form.is_valid():
            novo_exercicio = form.save(commit=False)
            novo_exercicio.treino = treino
            novo_exercicio.save()
            return redirect('workouts:treino_detalhes', pk=treino.pk)
    else:
        form = TreinoExercicioForm()

    context = {
        'treino': treino,
        'exercicios': exercicios,
        'form': form
    }
    return render(request, 'workouts/treino_detalhes.html', context)


@login_required
def treino_view(request, pk):
    treino = get_object_or_404(Treino, pk=pk)

    exercicios = TreinoExercicio.objects.filter(
        treino=treino).order_by('order')

    context = {
        'treino': treino,
        'exercicios': exercicios
    }
    return render(request, 'workouts/treino_view.html', context)
