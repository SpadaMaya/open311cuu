

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio', views.Inicio.as_view(), name='inicio' ),
    path('solicitudes', views.Solicitudes.as_view(), name='formulario'),
    path('eliminar-solicitud/<int:libro_id>/', views.EliminarSolicitud.as_view(), name='eliminar_solicitud'),
]