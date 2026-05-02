from django import forms
from .models import Treino, TreinoExercicio, Exercicio


class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ['student', 'title', 'description', 'day']

        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            # Você pode adicionar classes CSS aqui depois
        }


class TreinoExercicioForm(forms.ModelForm):
    class Meta:
        model = TreinoExercicio
        fields = ['exercicio', 'series', 'repetitions',
                  'weight', 'rest_seconds', 'order']


class ExercicioForm(forms.ModelForm):
    class Meta:
        model = Exercicio
        fields = ['title', 'description', 'category', 'difficulty']
