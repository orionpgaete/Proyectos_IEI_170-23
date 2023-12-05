from django.shortcuts import render
from .serializers import EstudianteSerial
from .models import Estudiante
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def estudiante_list(request):
    if request.method == 'GET':
        estudi = Estudiante.objects.all()
        serial = EstudianteSerial(estudi, many=True)
        return Response(serial.data)

    if request.method == 'POST':
        serial = EstudianteSerial(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)