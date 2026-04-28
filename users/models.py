# Importa recursos para criar modelos no banco de dados
from django.db import models

# Importa modelo base de usuário do Django
# (login, senha, permissões, nome etc.)
from django.contrib.auth.models import AbstractUser

# Importa validador personalizado de CPF
from .validators import validate_cpf

# Importa biblioteca de expressões regulares
import re


# ======================================================
# MODELO PERSONALIZADO DE USUÁRIO
# ======================================================
class User(AbstractUser):

    # ----------------------------------------------
    # Tipos de usuário permitidos no sistema
    # ----------------------------------------------
    ROLE_CHOICES = (
        ('teacher', 'Professor'),
        ('student', 'Aluno'),
    )

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    # ----------------------------------------------
    # Tipo do usuário
    # teacher = Professor
    # student = Aluno
    # ----------------------------------------------
    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default='student')

    cpf = models.CharField(max_length=11, unique=True,
                           validators=[validate_cpf], blank=True)

    # ==================================================
    # LOGIN SERÁ FEITO PELO EMAIL
    # ==================================================
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    # ==================================================
    # MÉTODO SAVE PERSONALIZADO
    # Executa antes de salvar no banco
    # ==================================================
    def save(self, *args, **kwargs):

        if self.cpf:
            self.cpf = re.sub(r'\D', '', self.cpf)

        self.username = self.email

        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
