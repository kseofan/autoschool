from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView
from users.models import Person, PersonType
from students.models import Student, SkillLevel, Lesson, Application


class PastLessonsListView(ListView):
    model = Lesson

    def get_context_data(self, **kwargs):
        context = super(PastLessonsListView, self).get_context_data(**kwargs)
        if not (isinstance(self.request.user, User) and self.request.user.is_authenticated()):
            return redirect('index')
        person = Person.objects.get(user=self.request.user)
        context['person'] = person
        return context


class FutureLessonsListView(ListView):
    model = Lesson

    def get_context_data(self, **kwargs):
        context = super(FutureLessonsListView, self).get_context_data(**kwargs)
        if not (isinstance(self.request.user, User) and self.request.user.is_authenticated()):
            return redirect('index')
        person = Person.objects.get(user=self.request.user)
        context['person'] = person
        return context
