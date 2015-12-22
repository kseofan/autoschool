from django.contrib.auth.models import User
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import timezone
from students.models import Student, Lesson
from users.models import Person


class ModularTestStudent(TestCase):

    def test_is_lesson_tomorrow(self):
        lesson_past = Lesson.objects.create(datetime=(timezone.now() + timezone.timedelta(hours=-12)))
        lesson_now = Lesson.objects.create(datetime=(timezone.now()))
        lesson_tomorrow = Lesson.objects.create(datetime=(timezone.now() + timezone.timedelta(hours=12)))
        lesson_far_future = Lesson.objects.create(datetime=(timezone.now() + timezone.timedelta(hours=36)))

        self.assertTrue(lesson_tomorrow.is_lesson_tomorrow())
        self.assertFalse(lesson_past.is_lesson_tomorrow())
        self.assertFalse(lesson_now.is_lesson_tomorrow())
        self.assertFalse(lesson_far_future.is_lesson_tomorrow())

    def test_get_lessons(self):
        student = Student.objects.create()
        lesson_1 = Lesson.objects.create(student=student)
        Lesson.objects.create()
        Lesson.objects.create()
        lesson_2 = Lesson.objects.create(student=student)

        self.assertListEqual(list(student.get_lessons()), [lesson_1, lesson_2])

    def test_profile(self):
        response = self.client.get(reverse('profile'))
        self.assertRedirects(response, '/')

        user = User.objects.create_user('user', 'user@localhost', 'test')
        person = Person.objects.create(user=user, type=0)
        Student.objects.create(person=person)
        self.client.login(username='user', password='test')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/profile.html')
