from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from apigenerica.api.models import Endpoint
from apigenerica.api.serializers import UserSerializer, GroupSerializer, EndpointSerializer

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class EndpointViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Endpoints to be viewed or edited.
    """
    queryset = Endpoint.objects.all().order_by('-fecha_alta')
    serializer_class = EndpointSerializer
    permission_classes = [permissions.IsAuthenticated]