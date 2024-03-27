from django.urls import path, include   
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    #______________________Menu principal______________________
    path('', home, name="home"),
    path('acerca/', acerca, name="acerca"),

    #______________________Blog______________________
    path('blog/', blog, name="blog"),
    path('blog_admin/', blogAdmin, name="blog_admin"),
    path('blog_create/', blogCreate, name="blog_create"),
    path('blog_update/<id_blog>', blogUpdate, name="blog_update"),
    path('blog_delete/<int:pk>', BlogDelete.as_view(), name="blog_delete"),

    #______________________Proyectos______________________
    path('proyectos/', proyectos, name="proyectos"),
    path('proyectos_admin/', proyectosAdmin, name="proyectos_admin"),
    path('proyectos_create/', proyectosCreate, name="proyectos_create"),
    path('proyectos_update/<id_proyectos>', proyectosUpdate, name="proyectos_update"),
    path('proyectos_delete/<int:pk>', ProyectosDelete.as_view(), name="proyectos_delete"),

    #______________________Eventos______________________
    path('eventos/', eventos, name="eventos"),
    path('eventos_admin/', eventosAdmin, name="eventos_admin"),
    path('eventos_create/', eventosCreate, name="eventos_create"),
    path('eventos_update/<id_eventos>', eventosUpdate, name="eventos_update"),
    path('eventos_delete/<int:pk>', EventosDelete.as_view(), name="eventos_delete"),

    #______________________Merchandising______________________
    path('merchandising/', MerchandisingList.as_view(), name="merchandising"),
    path('merchandising_admin/', merchandisingAdmin, name="merchandising_admin"),
    path('merchandising_create/', MerchandisingCreate.as_view(), name="merchandising_create"),
    path('merchandising_update/<int:pk>', MerchandisingUpdate.as_view(), name="merchandising_update"),
    path('merchandising_delete/<int:pk>', MerchandisingDelete.as_view(), name="merchandising_delete"),

    #________________________Busqueda de eventos_______________________
    path('buscar_eventos/', buscarEventos, name="buscar_eventos"),
    path('encontrar_eventos/', encontrarEventos, name="encontrar_eventos"),

    #________________________Login, Logout, Registration_______________________
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html") , name="logout"),
    path('registrar/', register, name="registrar"),

    #________________________Edición de Perfil, Cambio Clave, Avatar_______________________
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
]