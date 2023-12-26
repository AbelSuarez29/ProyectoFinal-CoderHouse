from django.shortcuts import render, redirect
from .forms import UserCreationFormulario, UserEditionFormulario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Avatar

def home(request):
    return render(request, 'usuarios/index.html')

#------REGISTRAR USUARIOS--------#

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

#---------EDITAR PERFIL-----------#

@login_required
def editar_perfil_view(request):
    usuario = request.user
    avatar = Avatar.objects.filter(user=usuario).first()
    avatar_url = avatar.imagen.url if avatar is not None else ""
    if request.method == "GET":
        valores_iniciales ={
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name
        }

        formulario = UserEditionFormulario(initial= valores_iniciales)
        return render(request,
                       "usuarios/editar_perfil.html",
                         context={"form": formulario, "usuario": usuario,
                                  "avatar_url": avatar_url})
    else:
        formulario = UserEditionFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data

            usuario.email = informacion["email"]
            usuario.set.password(informacion["password1"])
            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.save()
            return redirect("core:index")

def inicio_view(request):
    if request.user.is_authenticated:
        usuario = request.user
        avatar= Avatar.objects.filter(user=usuario).first()
        avatar_url = avatar.imagen.url if avatar is not None else ""
        return render(request, "core/index.html", context={"avatar_url": avatar_url})
    else:
        avatar_url= ""