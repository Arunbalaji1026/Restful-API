from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employee
from .serializers import employeeSerializer
from rest_framework import mixins
from rest_framework import generics

class indexList(APIView):

    def get(self, request, format=None):
        employe_info = employee.objects.all()
        serializer = employeeSerializer(employe_info, many=True)
        return Response(serializer.data)

    def post(self):
        pass
