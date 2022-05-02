from django.urls import path
from . import views
from django.config import settings
from django.config.urls.static import static

appname = "converter"

urlpatterns = [
        path('', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
