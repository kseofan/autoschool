from django.db import models
from django.contrib.auth.models import User


class PersonType():
    STUDENT = 0
    INSTRUCTOR = 1
    CURATOR = 2
    PERSON_TYPE_CHOICES = (
        (STUDENT, 'Student'),
        (INSTRUCTOR, 'Instructor'),
        (CURATOR, 'Curator'),
    )


class Person(models.Model):
    user = models.ForeignKey(User, unique=True)
    middle_name = models.TextField(blank=True, null=True)
    dateOfBirth = models.DateTimeField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    type = models.IntegerField(default=0, choices=PersonType.PERSON_TYPE_CHOICES)

    def __str__(self):
        if self.middle_name is not None:
            return self.user.last_name + ' ' + self.user.first_name + ' ' + self.middle_name
        else:
            return self.user.last_name + ' ' + self.user.first_name

    def birthday(self):
        return self.dateOfBirth.__format__('HH')
