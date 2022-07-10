from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from rest_framework.parsers import JSONParser

from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets
from .forms import CreateTaskForm


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def todo(request):
    form = CreateTaskForm()
    context = {'form': form}
    return render(request, 'index.html', context)

