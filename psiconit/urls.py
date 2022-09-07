"""proyectoa_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from psiconitApp import views
 
urlpatterns = [
   
   
    path('admin/', admin.site.urls),
    path('', views.index, name="Index"),
    path('inicio/', views.index, name="inicio"),
    path('juegos/', views.juego, name="juegos"),
    path('inmersiva/', views.inmersiva, name="inmersiva"),
    path('pagina-pruebas/', views.pagina, name="pagina"),
    path('contacto/', views.contacto, name="contacto"),
    path('registro/', views.register_page, name='register'),
    path('login/', views.login_page, name="login"),
    path('reporte/',views.reporte, name =  "reporte"),
    path('logout/',views.logout_user, name =  "logout"),
    path('listapacientes/',views.listar_pacientes, name =  "listapacientes")
   
]