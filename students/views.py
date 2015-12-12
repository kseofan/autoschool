from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.models import Person, PersonType
from students.models import Student, SkillLevel


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
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
    return redirect('profile')
