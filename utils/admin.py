# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *
from django.contrib.contenttypes import generic


class BaseAdmin(admin.ModelAdmin):
    list_display = ('label', 'created', 'modified')


class FileInline(generic.GenericTabularInline):
    model = File

admin.site.register(Reference, BaseAdmin)
admin.site.register(Category, BaseAdmin)
admin.site.register(Tag, BaseAdmin)
