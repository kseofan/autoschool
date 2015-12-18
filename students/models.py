from django.db import models
from users.models import Person
from instructors.models import Instructor
from django.utils import timezone


class SkillLevel():
    UNFAMILIAR = 0
    FAMILIAR = 1
    EXPERIENCED = 2
    SKILL_LEVEL_CHOICES = (
        (UNFAMILIAR, 'Unfamiliar'),
        (FAMILIAR, 'Familiar'),
        (EXPERIENCED, 'Experienced'),
    )


class Student(models.Model):
    person = models.ForeignKey(Person, null=True, unique=True)
    applications_limit = models.IntegerField(default=10)
    skill_level = models.IntegerField(default=0, choices=SkillLevel.SKILL_LEVEL_CHOICES)

    def clear_future_applications(self):
        lessons = Lesson.objects.filter(student=self).filter(datetime__gt=timezone.now())
        for lesson in lessons:
            if lesson.is_lesson_tomorrow() or lesson.is_lesson_passed():
                return False
        for lesson in lessons:
            lesson.student = None
            lesson.save()
        return True

    def get_applications_amount(self):
        return Lesson.objects.filter(student=self).filter(is_cancelable=False).count()

    def get_instructor(self):
        try:
            student_instructor = StudentInstructor.objects.filter(student=self).latest('apply_datetime')
            return student_instructor.instructor
        except StudentInstructor.DoesNotExist:
            return None

    def get_latest_lesson(self):
        try:
            return Lesson.objects.filter(student=self).latest('datetime')
        except Lesson.DoesNotExist:
            return None

    def __str__(self):
        return self.person.__str__() + ' (Студент)'


class StudentInstructor(models.Model):
    apply_datetime = models.DateTimeField(default=timezone.now())
    student = models.ForeignKey(Student)
    instructor = models.ForeignKey(Instructor)


class Lesson(models.Model):
    datetime = models.DateTimeField(null=False, default=timezone.now())
    hours = models.IntegerField(default=0)
    instructor = models.ForeignKey(Instructor, null=True)
    student = models.ForeignKey(Student, null=True, blank=True)

    def __str__(self):
        return 'Занятие инструктора ' + self.instructor.__str__() + ' ' + self.datetime.__str__()

    def is_lesson_tomorrow(self):
        return self.datetime > timezone.now() >= self.datetime + timezone.timedelta(hours=-24)

    def is_lesson_passed(self):
        return timezone.now() >= self.datetime
