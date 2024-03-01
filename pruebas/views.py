from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ArgentinaStateForm

def flex(request):
    return render(request, 'pruebas/flexbox0.html')

def wrap(request):
    return render(request, 'pruebas/flexbox-wrap0.html')

class ArgentinaStateFormView(FormView):
    template_name = 'pruebas/argentina_state_form.html'
    form_class = ArgentinaStateForm
    success_url = '/success/'

    def form_valid(self, form):
        form
        return super().form_valid(form)
    
