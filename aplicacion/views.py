from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import * 

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
#______________________Menu principal______________________
def home(request):
    return render(request, "aplicacion/index.html")

def acerca(request):
    return render(request, "aplicacion/acerca.html")

#______________________Blog______________________
def blog(request):
    contexto = {'blog': Blog.objects.all().order_by("id")}
    return render(request, "aplicacion/blog.html", contexto)

@login_required
def blogAdmin(request):
    contexto = {'blog': Blog.objects.all().order_by("id")}
    return render(request, "aplicacion/blog_admin.html", contexto)

@login_required
def blogCreate(request):
    if request.method == "POST":
        miForm = BlogForm(request.POST)
        if miForm.is_valid():
            blog_nombre = miForm.cleaned_data.get("nombre")
            blog_descripcion = miForm.cleaned_data.get("descripcion")
            blog_fecha = miForm.cleaned_data.get("fecha")
            blog_autor = miForm.cleaned_data.get("autor")
            blog = Blog(nombre=blog_nombre, descripcion=blog_descripcion, fecha=blog_fecha, autor=blog_autor)
            blog.save()
            return redirect(reverse_lazy('blog'))
    else:
        miForm = BlogForm()
    return render(request, "aplicacion/blogForm.html", {"form": miForm})

@login_required
def blogUpdate(request, id_blog):
    blog = Blog.objects.get(id=id_blog)
    if request.method == "POST":
        miForm = BlogForm(request.POST)
        if miForm.is_valid():
            blog.nombre = miForm.cleaned_data.get("nombre")
            blog.descripcion = miForm.cleaned_data.get("descripcion")
            blog.fecha = miForm.cleaned_data.get("fecha")
            blog.autor = miForm.cleaned_data.get("autor")
            blog.save()
            return redirect(reverse_lazy('blog'))
    else:
        miForm = BlogForm(initial={'nombre': blog.nombre, 'descripcion': blog.descripcion, 'fecha': blog.fecha, 'autor': blog.autor})
    return render(request, "aplicacion/blogForm.html", {"form": miForm})

class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("blog")

#______________________Proyectos______________________
def proyectos(request):
    contexto = {'proyectos': Proyectos.objects.all().order_by("id")}
    return render(request, "aplicacion/proyectos.html", contexto)

@login_required
def proyectosAdmin(request):
    contexto = {'proyectos': Proyectos.objects.all().order_by("id")}
    return render(request, "aplicacion/proyectos_admin.html", contexto)

@login_required
def proyectosCreate(request):
    if request.method == "POST":
        miForm = ProyectosForm(request.POST)
        if miForm.is_valid():
            proyectos_nombre = miForm.cleaned_data.get("nombre")
            proyectos_descripcion = miForm.cleaned_data.get("descripcion")
            proyectos_fecha = miForm.cleaned_data.get("fecha")
            proyectos = Proyectos(nombre=proyectos_nombre, descripcion=proyectos_descripcion, fecha=proyectos_fecha)
            proyectos.save()
            return redirect(reverse_lazy('proyectos'))
    else:
        miForm = ProyectosForm()
    return render(request, "aplicacion/proyectosForm.html", {"form": miForm})

@login_required
def proyectosUpdate(request, id_proyectos):
    proyectos = Proyectos.objects.get(id=id_proyectos)
    if request.method == "POST":
        miForm = ProyectosForm(request.POST)
        if miForm.is_valid():
            proyectos.nombre = miForm.cleaned_data.get("nombre")
            proyectos.descripcion = miForm.cleaned_data.get("descripcion")
            proyectos.fecha = miForm.cleaned_data.get("fecha")
            proyectos.save()
            return redirect(reverse_lazy('proyectos'))
    else:
        miForm = ProyectosForm(initial={'nombre': proyectos.nombre, 'descripcion': proyectos.descripcion, 'fecha': proyectos.fecha})
    return render(request, "aplicacion/proyectosForm.html", {"form": miForm})

class ProyectosDelete(LoginRequiredMixin, DeleteView):
    model = Proyectos
    success_url = reverse_lazy("proyectos")

#______________________Eventos______________________
def eventos(request):
    contexto = {'eventos': Eventos.objects.all().order_by("id")}
    return render(request, "aplicacion/eventos.html", contexto)

@login_required
def eventosAdmin(request):
    contexto = {'eventos': Eventos.objects.all().order_by("id")}
    return render(request, "aplicacion/eventos_admin.html", contexto)

@login_required
def eventosCreate(request):
    if request.method == "POST":
        miForm = EventosForm(request.POST)
        if miForm.is_valid():
            eventos_nombre = miForm.cleaned_data.get("nombre")
            eventos_organizador = miForm.cleaned_data.get("organizador")
            eventos_fecha = miForm.cleaned_data.get("fecha")
            eventos_formato = miForm.cleaned_data.get("formato")
            eventos = Eventos(nombre=eventos_nombre, organizador=eventos_organizador, fecha=eventos_fecha, formato=eventos_formato)
            eventos.save()
            return redirect(reverse_lazy('eventos'))
    else:
        miForm = EventosForm()
    return render(request, "aplicacion/eventosForm.html", {"form": miForm})

@login_required
def eventosUpdate(request, id_eventos):
    eventos = Eventos.objects.get(id=id_eventos)
    if request.method == "POST":
        miForm = EventosForm(request.POST)
        if miForm.is_valid():
            eventos.nombre = miForm.cleaned_data.get("nombre")
            eventos.organizador = miForm.cleaned_data.get("organizador")
            eventos.fecha = miForm.cleaned_data.get("fecha")
            eventos.formato = miForm.cleaned_data.get("formato")
            eventos.save()
            return redirect(reverse_lazy('eventos'))
    else:
        miForm = EventosForm(initial={'nombre': eventos.nombre, 'organizador': eventos.organizador, 'fecha': eventos.fecha, 'formato': eventos.formato})
    return render(request, "aplicacion/eventosForm.html", {"form": miForm})

class EventosDelete(LoginRequiredMixin, DeleteView):
    model = Eventos
    success_url = reverse_lazy("eventos")

#______________________Merchandising______________________
class MerchandisingList(ListView):
    model = Merchandising

@login_required
def merchandisingAdmin(request):
    contexto = {'merchandising': Merchandising.objects.all().order_by("id")}
    return render(request, "aplicacion/merchandising_admin.html", contexto)

class MerchandisingCreate(LoginRequiredMixin, CreateView):
    model = Merchandising
    fields = ["nombre", "valoraciones", "descripcion", "precio", "descuento", "delivery"]
    success_url = reverse_lazy("merchandising")

class MerchandisingUpdate(LoginRequiredMixin, UpdateView):
    model = Merchandising
    fields = ["nombre", "valoraciones", "descripcion", "precio", "descuento", "delivery"]
    success_url = reverse_lazy("merchandising")

class MerchandisingDelete(LoginRequiredMixin, DeleteView):
    model = Merchandising
    success_url = reverse_lazy("merchandising")

#________________________Busqueda de blog_______________________
def buscarEventos(request):
    return render(request, "aplicacion/index.html")

def encontrarEventos(request):
    if 'buscar' in request.GET:
        patron = request.GET["buscar"]
        eventos = Eventos.objects.filter(nombre__icontains=patron)
        contexto = {"eventos": eventos}
        return render(request, "aplicacion/eventos.html", contexto)
    
    contexto = {'eventos': Eventos.objects.all()}
    return render(request, "aplicacion/eventos.html", contexto)

#________________________Login, Logout, Authentication, Registration_______________________
def login_request(request):         
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            #_________________________Avatar_________________________
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar  
            #________________________________________________________
            return render(request, "aplicacion/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm} )

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": miForm} )

#________________________Edición de Perfil, Cambio Clave, Avatar_______________________
@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)

        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = UserEditForm(instance=usuario)

    return render(request, "aplicacion/editarPerfil.html", {"form": miForm} )

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "aplicacion/cambiar_clave.html"
    success_url = reverse_lazy("home")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=usuario)

            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            avatar = Avatar(user=usuario, imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('home'))
    else:
        miForm = AvatarForm()

    return render(request, "aplicacion/agregarAvatar.html", {"form": miForm} )