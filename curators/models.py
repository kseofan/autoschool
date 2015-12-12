from django.db import models
from users.models import Person


class Curator(models.Model):
    person = models.ForeignKey(Person, null=True)

    def __str__(self):
        return self.person.__str__() + ' (Куратор)'
