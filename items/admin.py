# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *
from utils.admin import FileInline


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_begin', 'date_end',
        'created', 'modified')
    inlines = [FileInline, ]
    search_fields = ['name', ]


class MarketInline(admin.TabularInline):
    model = Market
    inlines = [FileInline, ]
    extra = 0


class PictureInline(admin.TabularInline):
    model = Picture
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    list_display = ('label', 'created', 'modified')
    date_hierarchy = 'date'
    list_filter = ('persons', 'events', 'tags')
    search_fields = ['label', ]
    inlines = [PictureInline, MarketInline, FileInline]


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
        'name', 'created', 'modified')
    list_filter = ('role', )
    inlines = [FileInline, ]
    search_fields = ['first_name', 'last_name', 'name']


admin.site.register(Person, PersonAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Item, ItemAdmin)
