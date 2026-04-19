# Importa recursos para criação de models no Django
from django.db import models

# Importa model base do projeto
# Geralmente contém campos como:
# id, created_at, updated_at, active etc.
from core.models import Base

# Importa modelo de usuário
from users.models import User


# ======================================================
# MODELO EXERCÍCIO
# Cadastro de exercícios disponíveis no sistema
# ======================================================
class Exercicio(Base):

    # Nome do exercício
    # Ex: Supino, Agachamento, Rosca Direta
    title = models.CharField(
        'Título',
        max_length=100
    )

    # Descrição opcional do exercício
    # Ex: manter postura reta, descer controlado...
    description = models.TextField(
        'Descrição',
        blank=True
    )

    # Categoria muscular / tipo
    category = models.CharField(
        'Categoria',
        max_length=30,
        choices=[
            ('peito', 'Peito'),
            ('costas', 'Costas'),
            ('perna', 'Perna'),
            ('ombro', 'Ombro'),
            ('biceps', 'Bíceps'),
            ('triceps', 'Tríceps'),
            ('abdomen', 'Abdômen'),
            ('cardio', 'Cardio'),
        ]
    )

    # Nível de dificuldade
    difficulty = models.CharField(
        'Nível',
        max_length=20,
        choices=[
            ('iniciante', 'Iniciante'),
            ('intermediario', 'Intermediário'),
            ('avancado', 'Avançado'),
        ],
        default='iniciante'
    )

    # Campo futuro para vídeo demonstrativo
    # video_url = models.URLField(blank=True)

    # Define se exercício está ativo no sistema
    active = models.BooleanField(default=True)

    # Texto exibido no admin e consultas
    def __str__(self):
        return self.title


# ======================================================
# MODELO TREINO
# Treino criado por professor para aluno
# ======================================================
class Treino(Base):

    # Aluno dono do treino
    # Só permite usuários role=student
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'}
    )

    # Professor criador do treino
    # related_name permite:
    # professor.treinos_criados.all()
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='treinos_criados',
        limit_choices_to={'role': 'teacher'}
    )

    # Nome do treino
    title = models.CharField(max_length=100)

    # Observações / descrição
    description = models.TextField(blank=True)

    # Dia da semana do treino
    day = models.CharField(
        max_length=20,
        choices=[
            ('segunda', 'Segunda'),
            ('terca', 'Terça'),
            ('quarta', 'Quarta'),
            ('quinta', 'Quinta'),
            ('sexta', 'Sexta'),
            ('sabado', 'Sábado'),
            ('domingo', 'Domingo'),
        ]
    )

    # Treino ativo/inativo
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# ======================================================
# MODELO RELACIONAMENTO TREINO x EXERCÍCIO
# Cada treino pode ter vários exercícios
# ======================================================
class TreinoExercicio(Base):

    # Qual treino recebe o exercício
    treino = models.ForeignKey(
        Treino,
        on_delete=models.CASCADE
    )

    # Exercício vinculado
    exercicio = models.ForeignKey(
        Exercicio,
        on_delete=models.CASCADE
    )

    # Quantidade de séries
    series = models.IntegerField(default=3)

    # Quantidade de repetições
    repetitions = models.IntegerField(default=12)

    # Peso usado no exercício
    # Ex: 25.50 kg
    weight = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )

    # Descanso entre séries (segundos)
    rest_seconds = models.IntegerField(default=60)

    # Ordem do exercício no treino
    # Ex: 1º, 2º, 3º...
    order = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.treino} - {self.exercicio}'

    # Regras extras do banco
    class Meta:

        # Impede repetir mesma ordem dentro do treino
        # Ex: dois exercícios ordem=1 no mesmo treino
        unique_together = ('treino', 'order')
