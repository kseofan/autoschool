from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.generic import ListView
from users.models import Person
from students.models import Lesson
from instructors.models import Instructor


class FullInstructorsListView(ListView):
    model = Instructor

    def get_context_data(self, **kwargs):
        instructors = self.get_queryset()
        lessons = {}
        for instructor in instructors:
            lessons[instructor.pk] = Lesson.objects.filter(instructor=instructor).order_by('datetime')
        context = super(FullInstructorsListView, self).get_context_data(**kwargs)
        if not (isinstance(self.request.user, User) and self.request.user.is_authenticated()):
            return redirect('index')
        person = Person.objects.get(user=self.request.user)
        context['person'] = person
        context['lessons'] = lessons
        return context
