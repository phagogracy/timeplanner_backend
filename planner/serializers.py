from rest_framework import serializers

from .models import Project, Task
from user.serializers import UserShortSerializer
from user.models import User
from core.fields import ZenModelSerializeIntegerField


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for Project
    """

    class Meta:
        """
        Meta Class
        """

        model = Project
        fields = "__all__"

class ProjectShortSerializer(serializers.ModelSerializer):
    """
    Short Serializer for Project
    """

    class Meta:
        """
        Meta Class
        """

        model = Project
        fields = (
            "id",
            "title"
        )

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task
    """
    assigned_to = ZenModelSerializeIntegerField(model=User, serializer=UserShortSerializer)
    project = ZenModelSerializeIntegerField(model=Project, serializer=ProjectShortSerializer)

    class Meta:
        """
        Meta Class
        """

        model = Task
        fields = "__all__"
