from django.db import models

class Tabac(models.Model):
    brand = models.CharField(max_length=30)
    flavor = models.CharField(max_length=30, blank=True, null=True)
    empty = models.BooleanField(default=True)

    def __str__(self):
        brand = self.brand
        flavor = self.flavor or ''
        empty = 'Нет в наличии' if self.empty else 'В наличии'
        return f'{brand} {flavor} {empty}'