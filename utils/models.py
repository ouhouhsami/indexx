# -*- coding: utf-8 -*-
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Reference(TimeStampedModel):
    label = models.CharField(max_length=255)

    def __unicode__(self):
        return self.label


class Category(TimeStampedModel):
    label = models.CharField(max_length=255)

    def __unicode__(self):
        return self.label


class Tag(TimeStampedModel):
    label = models.CharField(max_length=255)

    def __unicode__(self):
        return self.label


class File(TimeStampedModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to="file")
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
