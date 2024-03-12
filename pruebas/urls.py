from django.urls import path
from django.views.generic import TemplateView, RedirectView
from .views import Temp2View

app_name='pruebas'

urlpatterns = [
    path('temp/', TemplateView.as_view(template_name='pruebas/temp.html', extra_context={'title':'Proyecto Siete'})),
    path('lista/', Temp2View.as_view(), name='temp2'), #View BASED on Template Views. Check View file.
    path('redt/', RedirectView.as_view())
]   