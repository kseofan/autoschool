from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView
from users.models import Person, PersonType
from students.models import Student, SkillLevel, Lesson, Application
from instructors.models import Instructor


class LessonsListView(ListView):
    model = Lesson

    def get_context_data(self, **kwargs):
        context = super(LessonsListView, self).get_context_data(**kwargs)
        if not (isinstance(self.request.user, User) and self.request.user.is_authenticated()):
            return redirect('index')
        person = Person.objects.get(user=self.request.user)
        context['person'] = person
        return context


class InstructorsListView(ListView):
    model = Instructor

    def get_context_data(self, **kwargs):
        context = super(InstructorsListView, self).get_context_data(**kwargs)
        if not (isinstance(self.request.user, User) and self.request.user.is_authenticated()):
            return redirect('index')
        person = Person.objects.get(user=self.request.user)
        context['person'] = person
        return context


def profile(request):
    if not (isinstance(request.user, User) and request.user.is_authenticated()):
        return redirect('index')
    person = Person.objects.get(user=request.user)
    if not person.type == PersonType.STUDENT:
        return redirect('index')
    student = Student.objects.get(person=person)

    context = {'person': person, 'student': student, 'skill_level': SkillLevel}
    return render(request, 'students/profile.html', context)


def change_profile(request):
    if request.method == "POST":
        person = Person.objects.get(user=request.user)
        person.middle_name = request.POST['middle_name']
        person.phone = request.POST['phone']
        person.save()

        student = Student.objects.get(person=person)
        student.skill_level = request.POST['skill_level']
        student.save()

    return redirect('profile')
