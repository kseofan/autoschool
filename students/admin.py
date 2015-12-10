from django.contrib import admin
from students.models import Student, StudentInstructor, Lesson, Application


admin.site.register(Student)
admin.site.register(StudentInstructor)
admin.site.register(Lesson)
admin.site.register(Application)
