from django.db import models
from users.models import Person


class Instructor(models.Model):
    person = models.ForeignKey(Person, null=True)
    automobile = models.TextField(blank=True)

    def __str__(self):
        return self.person.__str__() + ' (Инструктор)'
