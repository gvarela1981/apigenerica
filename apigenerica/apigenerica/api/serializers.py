from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apigenerica.api.models import Endpoint


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class EndpointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Endpoint
        fields = ['fecha_alta', 'servicio', 'title', 'url']
