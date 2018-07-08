# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "description", "price"]
    search_fields = ["description", "title"]
    list_filter = ['price', 'sale_price']
    list_editable = ["sale_price"]

    class Meta:
        model= Product