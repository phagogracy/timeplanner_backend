from rest_framework import serializers

from .models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):
    """ "
    Serializer for Project
    """

    class Meta:
        """
        Meta Class
        """

        model = Project
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    """ "
    Serializer for Task
    """

    class Meta:
        """
        Meta Class
        """

        model = Task
        fields = "__all__"
