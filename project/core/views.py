from django.shortcuts import render, redirect
from .models import NoticiaVideojuego

def home(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, "core/about.html")


from .models import NoticiaVideojuego

def index(request):
    return render(request, 'index.html')

def guardar_noticia(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fecha = request.POST.get('fecha')
        # Aquí guardas la noticia en la base de datos
        NoticiaVideojuego.objects.create(titulo=titulo, descripcion=descripcion, fecha=fecha)
        # Puedes redirigir a otra página o simplemente refrescar la misma
        return redirect('core:index')

def buscar_noticia(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre')
        # Aquí realizas la búsqueda por nombre en la base de datos
        noticias = NoticiaVideojuego.objects.filter(titulo__icontains=nombre)
        # Puedes pasar el resultado de la búsqueda a tu template
        return render(request, 'index.html', {'noticias': noticias})