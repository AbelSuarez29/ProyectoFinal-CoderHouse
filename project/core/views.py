from django.shortcuts import render, redirect
from .models import NoticiaVideojuego
from .forms import BuscarNoticia

def home(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, "core/about.html")


#---------DB DE NOTICIAS DE VIDEOJUEGOS-----------#
from django.contrib.auth.decorators import login_required

def videojuegos_view(request):

    if request.method == "GET":
        print("+"*90)
        print("+"*90)
        return render(
            request,
            "core/index.html",
        )
    else:   
        from .models import NoticiaVideojuego

        modelo = NoticiaVideojuego(titulo= request.POST["titulo"], descripcion= request.POST["descripcion"], fecha=request.POST["fecha"])
        modelo.save()
        return redirect("core:index")
    
@login_required
def videojuegos_todos_view(request):
    todas_las_noticias= []
    for noticias in NoticiaVideojuego.objects.all():
        todas_las_noticias.append(noticias)
    contexto = {"noticias": todas_las_noticias}
    return render(request, "core/noticias_todas.html", contexto)

#---------BUSCAR EN LA DB-----------#

def buscar_noticia(request):
    if request.method == "GET":
        form = BuscarNoticia()
        return render(
            request,
            "core/noticias_todas.html",
            context={"form": form}
        )
    else:   
        formulario = BuscarNoticia()
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            noticias_filtradas = []
            for noticias in NoticiaVideojuego.objects.filter(noticias= informacion["titulo"]):
                noticias_filtradas.append(noticias)
            # modelo = NoticiaVideojuego(titulo= informacion["titulo"], descripcion= informacion["descripcion"],
            #                            fecha= informacion["fecha"])
        # contexto = {"noticias": noticias_filtradas}
        # return render(request, "core/noticias_todas.html", contexto)
    
