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

    # ----------------------------------------------
    # Campo username
    # Herdado do AbstractUser, mas redefinido
    # ----------------------------------------------
    username = models.CharField(
        max_length=150,
        unique=True
    )

    # ----------------------------------------------
    # Campo e-mail único
    # Será usado para login
    # ----------------------------------------------
    email = models.EmailField(
        unique=True
    )

    # ----------------------------------------------
    # Tipo do usuário
    # teacher = Professor
    # student = Aluno
    # ----------------------------------------------
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='student'
    )

    # ----------------------------------------------
    # CPF do usuário
    # unique=True  -> não repete
    # validators   -> valida CPF
    # blank=True   -> pode ficar vazio no formulário
    # ----------------------------------------------
    cpf = models.CharField(
        max_length=11,
        unique=True,
        validators=[validate_cpf],
        blank=True
    )

    # ==================================================
    # LOGIN SERÁ FEITO PELO EMAIL
    # ==================================================
    USERNAME_FIELD = 'email'

    # Campos obrigatórios ao criar superusuário
    REQUIRED_FIELDS = ['username']

    # ==================================================
    # MÉTODO SAVE PERSONALIZADO
    # Executa antes de salvar no banco
    # ==================================================
    def save(self, *args, **kwargs):

        # Se CPF existir:
        if self.cpf:

            # Remove pontos, traços e caracteres não numéricos
            # Ex: 111.222.333-44 -> 11122233344
            self.cpf = re.sub(r'\D', '', self.cpf)

        # Define username igual ao email automaticamente
        self.username = self.email

        # Salva normalmente chamando método pai
        super().save(*args, **kwargs)

    # ==================================================
    # REPRESENTAÇÃO DO OBJETO
    # ==================================================
    def __str__(self):

        # Mostra email ao imprimir usuário
        return self.email
