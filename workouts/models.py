from django.db import models
from core.models import Base
from users.models import User


# ======================================================
# MODELO EXERCÍCIO
# Cadastro de exercícios disponíveis no sistema
# ======================================================
class Exercicio(Base):

    title = models.CharField('Título', max_length=100)
    description = models.TextField('Descrição', blank=True)

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
    difficulty = models.CharField('Nível', max_length=20, choices=[
        ('iniciante', 'Iniciante'),
        ('intermediario', 'Intermediário'),
        ('avancado', 'Avançado'),
    ], default='iniciante'
    )

    # Campo futuro para vídeo demonstrativo
    # video_url = models.URLField(blank=True)

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
        User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})

    # Professor criador do treino
    # related_name permite:
    # professor.treinos_criados.all()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='treinos_criados', limit_choices_to={'role': 'teacher'})
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    day = models.CharField(max_length=20, choices=[
        ('segunda', 'Segunda'),
        ('terca', 'Terça'),
        ('quarta', 'Quarta'),
        ('quinta', 'Quinta'),
        ('sexta', 'Sexta'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ])

    def __str__(self):
        return self.title


# ======================================================
# MODELO RELACIONAMENTO TREINO x EXERCÍCIO
# Cada treino pode ter vários exercícios
# ======================================================
class TreinoExercicio(Base):

    # Qual treino recebe o exercício
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)
    series = models.IntegerField(default=1)
    repetitions = models.IntegerField(default=12)
    weight = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    rest_seconds = models.IntegerField(default=30)
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
