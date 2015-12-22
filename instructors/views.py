from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic import ListView
from users.models import Person
from students.models import Lesson


class PastLessonsListView(ListView):
    model = Lesson

    def get_queryset(self):
        result_queryset = Lesson.objects.filter(datetime__lt=timezone.now())
        return result_queryset

    def get_context_data(self, **kwargs):
        context = super(PastLessonsListView, self).get_context_data(**kwargs)
        if not (isinstance(self.request.user, User) and self.request.user.is_authenticated()):
            return redirect('index')
        person = Person.objects.get(user=self.request.user)
        context['person'] = person
        return context


class FutureLessonsListView(ListView):
    model = Lesson

    def get_queryset(self):
        result_queryset = Lesson.objects.filter(datetime__gt=timezone.now())
        return result_queryset

    def get_context_data(self, **kwargs):
        context = super(FutureLessonsListView, self).get_context_data(**kwargs)
        if not (isinstance(self.request.user, User) and self.request.user.is_authenticated()):
            return redirect('index')
        person = Person.objects.get(user=self.request.user)
        context['person'] = person
        return context


def set_hours(request):
    if request.method == "POST":
        hours = request.POST['hours']
        lesson = Lesson.objects.get(pk=request.POST['lesson_id'])
        try:
            float_hours = float(hours)
            if float_hours < 0:
                float_hours = 0
            lesson.hours = float_hours
        except ValueError:
            lesson.hours = 0
        lesson.save()

    return redirect('past_lessons')
