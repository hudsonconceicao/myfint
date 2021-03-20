from django.db import models


class Goods(models.Model):
    """This class define Goods"""
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=500)
    type_good = models.ForeignKey(
        'TypeGoods',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
