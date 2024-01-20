from django.db.models import CharField, Manager, Model, URLField
from django_better_admin_arrayfield.models.fields import ArrayField  # type: ignore
from django_bleach.models import BleachField  # type: ignore


class Project(Model):
    title = CharField(max_length=128)
    subtitle = BleachField()
    description = BleachField()
    tags = ArrayField(CharField(max_length=64))
    repo_url = URLField()
    website = URLField()
    logo_url = URLField(blank=True, null=True, default=None)

    objects = Manager()
