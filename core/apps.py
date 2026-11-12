from django.apps import AppConfig
from django.db import models


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
     nome = models.CharField(max_length=100)
     cracha_id = models.IntegerField(unique=True)
     ativo = models.BooleanField(default=True)
