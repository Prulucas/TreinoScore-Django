from django.shortcuts import render, redirect
from .models import Treino, TreinoExercicio, Exercicio
from .forms import TreinoForm, TreinoExercicioForm, ExercicioForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from users.permissions import is_teacher_or_admin


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

    exercicios = Exercicio.objects.all().order_by('title')

    context = {
        'treinos': treinos,
        'exercicios': exercicios,
    }
    return render(request, 'workouts/listar_treinos.html', context)
# Criar treino (professor)

# Views de Treino_exercicio


@login_required
@user_passes_test(is_teacher_or_admin, login_url='workouts:workout_index')
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
@user_passes_test(is_teacher_or_admin, login_url='workouts:workout_index')
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


# Views de Exercicios

    if request.user.role == 'teacher':
        exercicios = Exercicio.objects.filter(
            teacher=request.user).order_by('-created')
    else:
        exercicios = Exercicio.objects.filter(
            student=request.user).order_by('title')

    return render(request, 'workouts/listar_exercicios.html', {'exercicios': exercicios})


@login_required
@user_passes_test(is_teacher_or_admin, login_url='workouts:workout_index')
def exercicio_create(request):
    if request.method == 'POST':
        form = ExercicioForm(request.POST)

        if form.is_valid():
            exercicio = form.save(commit=False)
            exercicio.teacher = request.user
            exercicio.save()
            return redirect('workouts:workout_index')
        # mudar

    else:
        form = ExercicioForm()
    context = {'form': form}
    return render(request, 'workouts/exercicio_form.html', context)


@login_required
def exercicio_detalhes(request, pk):
    exercicio = get_object_or_404(Exercicio, pk=pk)
    exercicios = TreinoExercicio.objects.filter(
        exercicio=exercicio).order_by('order')

    if request.method == 'POST':
        form = TreinoExercicioForm(request.POST)

        if form.is_valid():
            novo_exercicio = form.save(commit=False)
            novo_exercicio.exercicio = exercicio
            novo_exercicio.save()
            return redirect('workouts:exercicio_detalhes', pk=exercicio.pk)
    else:
        form = TreinoExercicioForm()

    context = {
        'exercicio': exercicio,
        'form': form
    }
    return render(request, 'workouts/exercicio_detalhes.html', context)
