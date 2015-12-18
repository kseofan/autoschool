from django.conf.urls import include, url
from django.contrib import admin
from users.views import index, action_login, action_logout, change_password
from students.views import profile, change_profile, InstructorsListView, LessonsListView, change_instructor, apply_lesson, cancel_lesson
from instructors.views import PastLessonsListView, FutureLessonsListView, set_hours
from curators.views import FullInstructorsListView


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^logout/', action_logout, name='logout'),
    url(r'^login/', action_login, name='login'),
    url(r'^change_password/', change_password, name='change_password'),
    url(r'^profile/', profile, name='profile'),
    url(r'^change_profile/', change_profile, name='change_profile'),
    url(r'^instructors', InstructorsListView.as_view(), name='instructors'),
    url(r'^change_instructor', change_instructor, name='change_instructor'),
    url(r'^lessons', LessonsListView.as_view(), name='lessons'),
    url(r'^apply_lesson', apply_lesson, name='apply_lesson'),
    url(r'^cancel_lesson', cancel_lesson, name='cancel_lesson'),
    url(r'^instructor/lessons/past', PastLessonsListView.as_view(template_name='students/past_lesson_list.html'), name='past_lessons'),
    url(r'^set_hours', set_hours, name='set_hours'),
    url(r'^instructor/lessons/future', FutureLessonsListView.as_view(template_name='students/future_lesson_list.html'), name='future_lessons'),
    url(r'^curator/instructors', FullInstructorsListView.as_view(template_name='instructors/full_instructor_list.html'), name='curator_list'),
    url(r'^admin/', include(admin.site.urls)),
]
