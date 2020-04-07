from django.db import models

class Endpoint(models.Model):
    fecha_alta = models.DateTimeField(auto_now_add=True)
    servicio = models.CharField(max_length=100, blank=True, default='')
    title = models.CharField(max_length=100, blank=True, default='')
    url = models.TextField()
    
    class Meta:
        ordering = ['fecha_alta']