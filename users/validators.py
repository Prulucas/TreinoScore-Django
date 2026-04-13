from django.core.exceptions import ValidationError
from validate_docbr import CPF


def validate_cpf(value):
    cpf = CPF()
    if not cpf.validate(value):
        raise ValidationError('CPF inválido')
