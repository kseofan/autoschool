from django.conf.urls import include, url
from django.contrib import admin
from users.views import index, action_login, action_logout
from students.views import profile, change_profile


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^logout/', action_logout, name='logout'),
    url(r'^login/', action_login, name='login'),
    url(r'^profile/', profile, name='profile'),
    url(r'^change_profile/', change_profile, name='change_profile'),
    url(r'^admin/', include(admin.site.urls)),
]
