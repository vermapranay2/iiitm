from django.conf.urls import url
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required


from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ipg/$', views.ipg, name='ipg'),
    url(r'^mtech/$', views.mtech, name='mtech'),
    url(r'^mba/$', views.mba, name='mba'),
    url(r'^phd/$', views.phd, name='phd'),
    url(r'^(?P<student_id>[0-9]+)/$', views.profile, name='profile'),
    url(r'^profile/add$', login_required(views.ProfileCreate.as_view(), login_url='/register'), name='profile-add'),
    url(r'^profile/(?P<pk>[0-9]+)/', login_required(views.ProfileUpdate.as_view(), login_url='/register'),
        name='profile-update'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^user_login$', views.user_login, name='user_login'),
    url(r'user_logout', views.user_logout, name='user_logout'),
    url(r'alumni', views.alumni, name='alumni'),
]
