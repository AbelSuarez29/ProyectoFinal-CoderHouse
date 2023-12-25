from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from .forms import UserCreationFormulario

def home(request):
    return render(request, 'usuarios/index.html')

def registro_view(request):
    if request.method == 'GET':
        return render(
            request,
            'usuarios/index.html',
            {"form": UserCreationFormulario()}
        )
    else:
        formulario = UserCreationFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            formulario.save()

            return render(
                request,
                "core/index.html",
                {"mensaje": f"usuario creado: {usuario}"}
            )
        else:
            return render(
                request,
                "usuarios/index.html",
                {"form": formulario}
            )