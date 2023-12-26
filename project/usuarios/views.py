from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from .forms import UserCreationFormulario

#------REGISTRAR USUARIOS--------#

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
                {"mensaje": f"Usuario creado: {usuario}"}
            )
        else:
            return render(
                request,
                "usuarios/index.html",
                {"form": formulario}
            )
        
#---------LOGIN VIEW-----------#
        
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def login_view(request):
    if request.user.is_authenticated:
        return render(
            request,
            "core/index.html",
            {"mensaje": f"Ya estás autenticado: {request.user.username}"}
        )
    
    if request.method == "GET":
        return render(
            request, 
            "usuarios/login.html",
            {"form": AuthenticationForm()}
        )
    else:
        formulario = AuthenticationForm(request, data = request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            password = informacion["password"]
            modelo = authenticate(username=usuario, password=password)
            login(request, modelo)
            return render(
                request,
                "core/index.html",
            {"mensaje": f"bienvenido {modelo.username}"}
            )
        else:
            return render(
                request,
                "usuario/login.html",
                {"form": formulario}
            )

def logout_view(request):
    pass
