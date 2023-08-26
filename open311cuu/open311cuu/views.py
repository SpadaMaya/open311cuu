from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect
from ..SolicitudesOPEN311 import forms 
from ..SolicitudesOPEN311.forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class Home(View):
    template_name = 'home.html'

    def post(self, request):
        return render(request, self.template_name)

def custom_logout(request):
    logout(request)
    return redirect('/SolicitudesOPEN311')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Corregido aquí
            return redirect('nombre_de_la_vista_o_url')  # Completa la URL o el nombre de la vista
        else:
            messages.error(request, 'Credenciales inválidas')
            return render(request, 'login.html')  # Cambia 'login' por el nombre correcto del template

def register(request):
    if request.method == 'POST':
        forms = UserRegistrationForm(request.POST)  # Asegúrate de haber definido UserRegistrationForm
        if form.is_valid():
            # Guardar datos del formulario en la bd
            form.save()
            #obtener nombre de usuario
            username = form.cleaned_data.get('username')
            #obtener contraseña
            password = form.cleaned_data.get('password')
            #autenticar
            user = authenticate(username=username, password=password)
            #iniciar sesión
            login(request, user)
            #redireccionar a pag de inicio
            return redirect('/libros/inicio')
    else:  # Este bloque "else" estaba mal indentado en tu código original
        form = UserRegistrationForm()  # Asigna el formulario en caso de solicitud no POST
    return render(request, 'registration/register.html', {'form': form})
                


