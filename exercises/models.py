from django.db import models
from core.models import Base


class Exercise(Base):
    REP_CHOICES = (
        ('8', '1 - 8 repetitions'),
        ('10', '1 - 10 repetitions'),
        ('12', '1 - 12 repetitions'),
        ('15', '1 - 15 repetitions'),
    )

    name = models.CharField('Name', max_length=100)
    repetitions = models.CharField(
        'Repetitions', max_length=2, choices=REP_CHOICES)
    description = models.TextField('Description', max_length=300)

    def __str__(self):
        return self.name
