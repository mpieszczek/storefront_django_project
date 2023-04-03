from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # What tag is aplied to what object
    # this is an instance of tag in object

    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # We want to do it in generic way
    # We dont want to create dependencies between apps. Here: between tags and store
    # Type o object
    # ID of object
    content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE)
    object_id = models.PositiveIntegerField() # we require IDs of foregin models to be integers
    content_object = GenericForeignKey() # reference to actual object