from django.db import models


class Base(models.Model):
    # só coloca valor ao criar
    created = models.DateField('Date of creation', auto_now_add=True)
    modify = models.DateField('Updated', auto_now=True)
    active = models.BooleanField('Active?', default=True)

    class Meta:
        abstract = True
