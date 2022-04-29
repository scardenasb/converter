from django.urls import path
from . import views

appname = "converter"

urlpatterns = [
        path('', views.index, name='index'),
]
