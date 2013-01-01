# -*- coding: utf-8 -*-
from django.db import models
from utils.models import *
from django_extensions.db.models import TimeStampedModel


class Person(TimeStampedModel):
    ROLE_CHOICES = (
        ('0', 'creator'),
        ('1', 'publisher'),
        ('2', 'creator and publisher'),
    )
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, blank=True, null=True)

    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return "%s %s %s %s" % (self.first_name, self.last_name, self.name, self.role)


class Event(TimeStampedModel):
    date_begin = models.DateField()
    date_end = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Item(TimeStampedModel):
    date = models.DateField(blank=True, null=True)
    label = models.CharField(max_length=255)
    persons = models.ManyToManyField(Person, blank=True, null=True)
    events = models.ManyToManyField(Event, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    def __unicode__(self):
        return self.label


class Picture(TimeStampedModel):
    item = models.ForeignKey(Item)
    reference = models.ForeignKey(Reference, blank=True, null=True)
    file = models.ImageField(upload_to='img')
    page = models.IntegerField(blank=True, null=True)
    vol = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)


class Market(TimeStampedModel):
    item = models.ForeignKey(Item)
    label = models.CharField(max_length=255)
    place = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    estimation_price = models.FloatField(blank=True, null=True)
    final_price = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return self.label
