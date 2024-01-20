from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin  # type: ignore

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ["title"]
