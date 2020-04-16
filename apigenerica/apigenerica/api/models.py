from django.db import models
from rest_framework import serializers

class Endpoint(models.Model):
	id = serializers.IntegerField(read_only=True)
	fecha_alta = models.DateTimeField(auto_now_add=True)
	servicio = models.CharField(max_length=20)
	url = models.CharField(max_length=100)
	descripcion = models.TextField(max_length=200, blank=True, default='')

	class Meta:
	    ordering = ['fecha_alta']