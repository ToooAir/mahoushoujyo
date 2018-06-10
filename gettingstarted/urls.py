from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views
import sitela.views
import mahoushoujyo.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url('admin/', admin.site.urls),
    url(r'^jerry/',include('jerry.urls')),
    url(r'^sitela/',include('sitela.urls')),
    url(r'^mahoushoujyo/', include('mahoushoujyo.urls')),
    url(r'search_form',sitela.views.search_form,name='search_form'),
    url(r'search',sitela.views.search, name='search'),
]
