from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Sum, Max, Avg

from .models import SolicitudesOPEN311
from .forms import SolicitudesOPEN311Form

def index(request):

    return HttpResponse("Hola mundo")

class Inicio(View):
    template_name = 'index.html'

    def post(self, request):
        form = SolicitudesOPEN311Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
        
        return render(request, self.template_name, {'form': form, 'SolicitudesOPEN311': SolicitudesOPEN311})
    
solicitudes = SolicitudesOPEN311.objects.all()

def enviar_solicitud(request):
    nueva_solicitud = SolicitudesOPEN311(
         titulo = "Espacio en construcción",
         categoria = "Espacio público",
         direccion = "Manuel Ojinaga #41293, Col. Arquitectos",
         descripcion = "La calle lleva cinco días inhábil",
         adjunto = "False" ,
    )
    nueva_solicitud.save()

    return HttpResponse('Solicitud enviada')

class Solicitudes(View):
    template_name = 'solicitudes.html'
    def get(self, request):
        form = SolicitudesOPEN311Form()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SolicitudesOPEN311Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
        
        return render(request, self.template_name, {'form': form})
            
class EliminarSolicitud(View):
    def post(self, request, solicitud_id):
        libro = get_object_or_404(Solicitudes, pk=solicitud_id)
        libro.delete()
        return redirect('inicio')
