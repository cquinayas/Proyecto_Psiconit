from tkinter.tix import Select
from django.shortcuts import render
from .forms import usuarioForm
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
#from proyectoa_formulario.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .models import usuario


def index(request):
    return render(request,'index.html',{
        'title':'Inicio'
    })

def juego(request):
    return render(request,'cognitiva.html',{
        'title':'Juegos'
    })

def inmersiva(request):
    return render(request,'inmersiva.html')

def pagina(request):
    return render(request,'pagina.html')

def contacto(request):
    return HttpResponse(layout2 +"""<h2>Contacto</h2>""")

  

def register_page(request):
    form = usuarioForm(request.POST or None)
    if form.is_valid():
        form.save()		
        messages.success(request, "Registro insertado correctamente")
        form = usuarioForm()
        return redirect('inicio')
    else:
        messages.error(request, 'Error al realizar el registro. Revise los datos.')
    context = {'form': form,
        'title' : 'Registro'
    }       
    return render(request, 'users/register.html', context)

def login_page(request):
    messages.warning(request, 'Primer mensaje del registro')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        #form = FormFactura(request, data=request.POST)
        #nombre_usuario = form.cleaned_data.get('username')
        #contra = form.cleaned_data.get('password')
        #user = authenticate(username = nombre_usuario, password = contra)
        

        if user is not None:
            login(request,user)
            messages.warning(request, 'Te has identificado correctamente')
            return redirect(to="inicio")
            

        else:
            messages.warning(request, 'No te has identificado correctamente')

    return render(request,'users/login.html',{
            'title' : 'Identificate'           
        })
    
def reporte(request):
    return render(request, 'users/reporte.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def listar_pacientes(request):
    pacientes = usuario.objects.all()
    return render (request, "users/listapacientes.html", {"pacientes": pacientes})