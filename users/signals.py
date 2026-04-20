# users/signals.py

# ======================================================
# SIGNALS DO APP USERS
# Responsável por ações automáticas após salvar usuário
# ======================================================

# Evento disparado após salvar qualquer model
from django.db.models.signals import post_save

# Decorator para registrar função que escuta signal
from django.dispatch import receiver

# Model de usuário personalizado
from users.models import User

# Model de treino
from workouts.models import Treino


# ======================================================
# CRIAR TREINOS AUTOMÁTICOS PARA NOVOS ALUNOS
# ======================================================
@receiver(post_save, sender=User)
def criar_treinos_iniciais(sender, instance, created, **kwargs):
    """
    Quando um novo usuário for criado:

    - Se for aluno (student)
    - E ainda não possuir treinos

    O sistema cria automaticamente:

    Treino A
    Treino B
    Treino C
    Treino D
    Treino E
    """

    # ----------------------------------------------
    # Se usuário foi apenas editado, não faz nada
    # ----------------------------------------------
    if not created:
        return

    # ----------------------------------------------
    # Apenas alunos recebem treino automático
    # ----------------------------------------------
    if instance.role != 'student':
        return

    # ----------------------------------------------
    # Segurança extra:
    # se já possui treino, não duplica
    # ----------------------------------------------
    if Treino.objects.filter(user=instance).exists():
        return

    # ----------------------------------------------
    # Lista de treinos padrão
    # ----------------------------------------------
    treinos_padrao = [
        {
            'title': 'Treino A',
            'description': 'Peito + Tríceps',
            'day': 'segunda',
        },
        {
            'title': 'Treino B',
            'description': 'Costas + Bíceps',
            'day': 'terca',
        },
        {
            'title': 'Treino C',
            'description': 'Perna completa',
            'day': 'quarta',
        },
        {
            'title': 'Treino D',
            'description': 'Ombro + Abdômen',
            'day': 'quinta',
        },
        {
            'title': 'Treino E',
            'description': 'Cardio + Mobilidade',
            'day': 'sexta',
        },
    ]

    # ----------------------------------------------
    # Cria cada treino no banco
    # ----------------------------------------------
    for treino in treinos_padrao:

        Treino.objects.create(
            user=instance,
            title=treino['title'],
            description=treino['description'],
            day=treino['day'],
            status='active'
        )
