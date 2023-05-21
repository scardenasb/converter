from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import AjaxUnit, Converter, AjaxResult

#appname = "converter"


urlpatterns = [
    path('', Converter.as_view(), name='converter'),
    path('ajax_view/', AjaxUnit.as_view(), name='ajax_view'),
    path('ajax_result/', AjaxResult.as_view(), name='ajax_result'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
