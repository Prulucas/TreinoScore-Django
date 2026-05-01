from django.contrib import admin
from .models import Exercicio, Treino, TreinoExercicio

admin.site.register(Exercicio)
admin.site.register(Treino)
admin.site.register(TreinoExercicio)
