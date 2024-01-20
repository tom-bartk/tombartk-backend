from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from tombartk.backend.serializers import (
    GroupSerializer,
    ProjectSerializer,
    UserSerializer,
)

from .models import Project


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint that allows projects to be viewed."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
