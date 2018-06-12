# -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Kamigurumi(models.Model):
    """Core product. Amigurumi made by"""
    birthday = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    size = models.FloatField()  # cm
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " " + str(self.birthday)


class KamigurumiImage(models.Model):
    """Images for our Kamigurumis."""
    kamigurumi = models.ForeignKey(Kamigurumi, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(unique=True)
