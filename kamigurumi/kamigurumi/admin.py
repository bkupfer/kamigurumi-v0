# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Category, Kamigurumi, KamigurumiImage


class KamigurumiImageInline(admin.TabularInline):
    model = KamigurumiImage
    extra = 3


class KamigurumiAdmin(admin.ModelAdmin):
    inlines = [ KamigurumiImageInline, ]


admin.site.register(Category)
admin.site.register(Kamigurumi, KamigurumiAdmin)
