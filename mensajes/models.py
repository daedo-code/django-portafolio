from django.db import models

class Mensaje(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('leido', 'Leído'),
        ('respondido', 'Respondido'),
    ]
    
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    asunto = models.CharField(max_length=150)
    cuerpo = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.asunto} ({self.estado})"

