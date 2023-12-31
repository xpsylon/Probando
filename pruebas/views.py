from django.shortcuts import render

def flex(request):
    return render(request, 'pruebas/flexbox0.html')

def wrap(request):
    return render(request, 'pruebas/flexbox-wrap0.html')
