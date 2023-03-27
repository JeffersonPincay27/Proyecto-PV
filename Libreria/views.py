from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import libro
from .forms import libroform


# Create your views here.

def inicio (request):
     return render(request, 'paginas/inicio.html')

def nosotros (request):
    return render(request, 'paginas/nosotros.html')

def libros (request):
    libros = libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros} )

def crear (request):
    formulario = libroform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar (request, id):
    mlibro= libro.objects.get(id=id)
    formulario=libroform(request.POST or None, request.FILES or None, instance=mlibro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request,'libros/editar.html',{'formulario':formulario})

def eliminar(request, id):
    mlibro= libro.objects.get(id=id)
    mlibro.delete()
    return redirect('libros')






