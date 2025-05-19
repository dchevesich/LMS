from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home_logeado_view(request):
    context = {
        'usuario_actual': request.user
    }
    return render(request, 'sitiologin/home_logeado.html', context)
