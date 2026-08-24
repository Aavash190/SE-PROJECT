from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


# We use ModelViewSet here because it automatically generates all CRUD operations.
# This prevents code repetition (DRY principle) and keeps the files short.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
