# Seperate URL file for searchApp application,
# keeps main urls.py clean

from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    # url(r'^$', views.search_page, name='home'),
    url(r'^$', views.search_page, name='search'),
    url(r'display_paper/(?P<object_id>\d+)/$', views.display_paper, name='paper'),
]

urlpatterns += staticfiles_urlpatterns()
