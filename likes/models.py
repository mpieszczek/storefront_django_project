from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User


class LikedItem(models.Model):
    # what user likes what object
    # What tag is aplied to what object
    # this is an instance of tag in object

    # USER
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # OBJECT
    content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE)
    object_id = models.PositiveIntegerField() # we require IDs of foregin models to be integers
    content_object = GenericForeignKey() # reference to actual object