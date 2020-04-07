from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from apigenerica.models import Endpoint
from apigenerica.serializers import EndpointSerializer

@csrf_exempt
def endopint_list(request):
    """
    List all endopints, or create a new endopint.
    """
    if request.method == 'GET':
        endpoints = Endpoint.objects.all()
        serializer = EndpointSerializer(endpoints, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EndpointSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def endpoint_detail(request, pk):
    """
    Retrieve, update or delete an endpoint.
    """
    try:
        endpoint = Endpoint.objects.get(pk=pk)
    except Endpoint.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EndpointSerializer(endpoint)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EndpointSerializer(endpoint, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        endpoint.delete()
        return HttpResponse(status=204)