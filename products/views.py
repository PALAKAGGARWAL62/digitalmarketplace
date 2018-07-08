# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Product
# Create your views here.


def detail_view(request):
    if request.user.is_authenticated():
        product = Product.object.all().first()
        print request
        template = "detail_view.html"
        context = {}
        return render(request, template, context)
    else:
        template = "not_found.html"
        context = {}
        return render(request, template, context)


def list_view(request):
    print request
    queryset = Product.objects.all()
    template = "list_view.html"
    context = {'''queryset = queryset'''}
    return render(request, template, context)
