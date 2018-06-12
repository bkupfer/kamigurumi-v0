# -*- coding: utf-8 -*-
from django.db import models


class Kamigurumi(models.Model):
    """Core product. Amigurumi made by"""
    img =
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    description = models.CharField(max_length=1024)
    category =
    sold
    size = models.FloatField()  # cm
