from django.conf.urls import url

from dragons import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]