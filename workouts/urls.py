from django.urls import path
from . import views

app_name = 'workouts'

urlpatterns = [
    # path('workouts', listar_treinos, name='workout'),
    path('', views.listar_treinos, name='workout_index'),
    path('create_workout/', views.treino_create, name='treino_form'),
    path('treino/<int:pk>/detalhes/',
         views.treino_detalhes, name='treino_detalhes'),
    path('treino/<int:pk>/', views.treino_view, name='treino_view'),
    path('create_exercise/', views.exercicio_create, name='exercicio_form'),

]
