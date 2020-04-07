from rest_framework import serializers
from apigenerica.models import Endpoint

class EndpointSerializer(serializers.ModelSerializer):
	class Meta:
		model = Endpoint
		fields = ['fecha_alta', 'title', 'servicio', 'url']
