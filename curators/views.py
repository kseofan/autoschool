from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView
from users.models import Person, PersonType
from students.models import Student, SkillLevel, Lesson
from instructors.models import Instructor


class FullInstructorsListView(ListView):
    model = Instructor

    def get_context_data(self, **kwargs):
        context = super(FullInstructorsListView, self).get_context_data(**kwargs)
        if not (isinstance(self.request.user, User) and self.request.user.is_authenticated()):
            return redirect('index')
        person = Person.objects.get(user=self.request.user)
        context['person'] = person
        return context
