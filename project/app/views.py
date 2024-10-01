from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def 