from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.ForeignKey(User)
    middle_name = models.TextField(blank=True, null=True)
    dateOfBirth = models.DateTimeField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.middle_name is not None:
            return self.user.last_name + ' ' + self.user.first_name + ' ' + self.middle_name
        else:
            return self.user.last_name + ' ' + self.user.first_name

    class Meta:
        abstract = True




