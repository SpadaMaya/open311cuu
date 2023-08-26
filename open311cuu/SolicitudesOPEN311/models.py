from django.db import models

# Modelo de campos en mi tabla: Categoría, Dirección, Descripción visual, Adjuntar dato

class SolicitudesOPEN311(models.Model):


    titulo = models.CharField("Título", max_length=300, default="Sin título")
    categoria = models.CharField("Categoría", max_length=300, default="Sin categoría")#Selectbox
    direccion = models.CharField("Dirección", max_length=300, default="Sin dirección")
    descripcion = models.CharField("Descripción general del problema", max_length=300, default="Sin descripción")
    adjunto = models.FileField("Archivo adjunto", upload_to='adjuntos/', blank=True, null=True)

    def __str__(self):
        return self.titulo
   