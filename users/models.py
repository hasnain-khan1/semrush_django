from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
from django.contrib.auth.models import User
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

import json
class Messages(models.Model):
    Body = models.CharField(max_length=5000)

    # def save(self,*args,**kwargs):
    #     print('this ois save')
    #     channel_layer = get_channel_layer()
    #     data={'here':'that is all because of Allah'}
    #     async_to_sync(channel_layer.group_send)(
    #         "messages_group", {
    #                 'type' : 'next_notifi',
    #                 'value' : json.dumps(data),
    #                 })
    #     super(Messages,self).save(*args,**kwargs)
# @receiver(post_save, sender=Messages, dispatch_uid="update_manager_admin")
# def new_message(sender, instance, **kwargs):
#     # if created:
#     channel_layer = get_channel_layer()
    
#     async_to_sync(channel_layer.group_send)(
#         "message", {
#                     "type": "new.message",
#                     "event": "New Message",
#                     "Body": "instance.Body",
#                     "Date": "instance.Body",
#                     "ConversationId": "instance.Body",
#                     })
#     print('asim razaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#     print('000000000000000000000000000000000000000000000')
