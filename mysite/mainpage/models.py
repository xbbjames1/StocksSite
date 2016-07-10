from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Stock(models.Model):
    symbol = models.CharField('symbol',max_length=100)
    price = models.IntegerField('price')
    
    def __str__(self):
        return self.symbol
