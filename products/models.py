# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Product (models.Model):
    title = models.CharField(max_length=40)
    item_id = models.IntegerField()
    description = models.TextField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=3, default=9.99)
    sale_price = models.DecimalField(max_digits=8, decimal_places=3, default=6.66)

    def __unicode__(self):
        return self.title
