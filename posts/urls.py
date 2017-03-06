from django.conf.urls import url

from . import views

app_name = 'posts'
urlpatterns = [
    url(r'^$', views.index, name='post_index'),
    url(r'^/create/$', views.create, name='create'),
]