from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
path("<int:id>", views.index, name="index"),
path("create/", views.create, name="create"),
path("", views.home, name="home"),
path("home", views.home, name="home"),
]


# Next part 9 2:21:10