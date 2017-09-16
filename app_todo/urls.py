from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
#    url(r'^add', views.add_db, name='add'),
    url(r'add', views.add_db, name='add'),
        ]
