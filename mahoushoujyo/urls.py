from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^404notfound/', views.notfound, name="notfound"),
    url(r'^signin/', views.signin, name="signin"),
    url(r'^register/', views.register, name="register"),
    url(r'^main/$', views.main, name="main"),
    url(r'^main/hide/$', views.hide, name="hide"),
    url(r'^main/hide/amplification/', views.amplification, name="amplification"),
]