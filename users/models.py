from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import Base
from .validators import validate_cpf
import re


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Professor'),
        ('student', 'Aluno'),
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='student'
    )

    cpf = models.CharField(
        max_length=11,
        unique=True,
        validators=[validate_cpf],
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if self.cpf:
            self.cpf = re.sub(r'\D', '', self.cpf)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
