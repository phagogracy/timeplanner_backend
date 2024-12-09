from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer


class ProjectAPISet(viewsets.ModelViewSet):
    """
    Model View Set for Project
    """

    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = []
    lookup_field = "pk"
    http_method_names = ("get", "post", "patch", "delete")
    filter_backends = (SearchFilter,)
    search_fields = ("title",)


class TaskAPISet(viewsets.ModelViewSet):
    """
    Model View Set for Task
    """

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = []
    lookup_field = "pk"
    http_method_names = ("get", "post", "patch", "delete")
    filter_backends = (SearchFilter,)
    search_fields = ("title",)
