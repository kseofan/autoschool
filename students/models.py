from django.db import models
from users.models import Person
from instructors.models import Instructor
from django.utils import timezone


class Student(Person):
    UNFAMILIAR = 0
    FAMILIAR = 1
    EXPERIENCED = 2
    SKILL_LEVEL_CHOICES = (
        (UNFAMILIAR, 'Unfamiliar'),
        (FAMILIAR, 'Familiar'),
        (EXPERIENCED, 'Experienced'),
    )
    applications_limit = models.IntegerField(default=10)
    skill_level = models.IntegerField(default=0, choices=SKILL_LEVEL_CHOICES)

    def clear_future_applications(self):
        applications = Application.objects.filter(student=self).filter(apply_datetime__gt=timezone.now())
        for application in applications:
            application.is_actual = False
            application.save()

    def get_applications_amount(self):
        return Application.objects.filter(student=self).filter(is_actual=True).count()


class StudentInstructor(models.Model):
    apply_datetime = models.DateTimeField(default=timezone.now())
    student = models.ForeignKey(Student)
    instructor = models.ForeignKey(Instructor)


class Lesson(models.Model):
    datetime = models.DateTimeField(null=False, default=timezone.now())
    hours = models.IntegerField(default=0)
    instructor = models.ForeignKey(Instructor)

    def __str__(self):
        return 'Занятие инструктора ' + self.instructor.__str__() + ' ' + self.datetime.__str__()

    def get_actual_application(self):
        return Application.objects.filter(lesson=self).latest(field_name='apply_datetime')

    def is_lesson_tomorrow(self):
        return timezone.now() >= self.datetime + timezone.timedelta(hours=-24)


class Application(models.Model):
    apply_datetime = models.DateTimeField(null=False, default=timezone.now())
    student = models.ForeignKey(Student)
    lesson = models.ForeignKey(Lesson)
    is_actual = models.BooleanField(default=True)
