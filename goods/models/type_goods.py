from django.db import models


class TypeGoods(models.Model):
    """This class define TypeGoods"""
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name