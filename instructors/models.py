from django.db import models
from users.models import Person


class Instructor(Person):
    automobile = models.TextField(blank=True)
