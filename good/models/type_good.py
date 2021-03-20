from django.db import models


class TypeGood(models.Model):
    """This class describle TypeGood"""
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
