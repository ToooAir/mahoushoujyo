from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import mahoushoujyo.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', mahoushoujyo.views.index, name='index'),
    url(r'^404notfound/', mahoushoujyo.views.notfound, name="notfound"),
    url(r'^signin/', mahoushoujyo.views.signin, name="signin"),
    url(r'^register/', mahoushoujyo.views.register, name="register"),
    url(r'^main/$', mahoushoujyo.views.main, name="main"),
    url(r'^main/hide/$', mahoushoujyo.views.hide, name="hide"),
    url(r'^main/hide/amplification/', mahoushoujyo.views.amplification, name="amplification"),
]
