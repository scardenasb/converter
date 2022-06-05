from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

appname = "converter"

urlpatterns = [
        path('', views.index, name='index'),
        path('ajax/load-units', views.load_units, name='ajax_load_units'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
