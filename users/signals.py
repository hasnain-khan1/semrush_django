from django.contrib.auth.models import User
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
# from .models import *
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from .models import *
from django.db.models.signals import post_save

def save_profile(sender, instance, **kwargs):
    # instance.profile.save()
    print('this is print')

post_save.connect(save_profile, sender=User)


@receiver(post_save, sender=Messages, dispatch_uid="update_manager_admin")
def age(sender, instance, **kwargs):
    # if created:
    print('asim razaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    # channel_layer = get_channel_layer()
    # con = Conversation.objects.filter(id=instance.conversation_id.id).select_related('contact_id','user_id').get()    
    # contact = con.contact_id
    # fromNumber = contact.number
    # async_to_sync(channel_layer.group_send)(
    #     "message", {
    #                 "MessageStatus": "instance.Body",
    #                 "Type": "instance.Body",
    #                 "Messagesid": "instance.Body",
    #                 "fromNumber" : "instance.Body"
    #             #    "PhoneNumber": instance.number
    #                 })

# @receiver(post_save, sender=Messages, dispatch_uid="update_manager_admin")
# def new_message(sender, instance, **kwargs):
#     # if created:
#     print('asim razaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#     channel_layer = get_channel_layer()
#     # con = Conversation.objects.filter(id=instance.conversation_id.id).select_related('contact_id','user_id').get()    
#     # contact = con.contact_id
#     # fromNumber = contact.number
#     async_to_sync(channel_layer.group_send)(
#         "message", {
#                     "type": "new.message",
#                     "event": "New Message",
#                     "Body": "instance.Body",
#                     "Date": "instance.Body",
#                     "ConversationId": "instance.Body",
#                     "MessageStatus": "instance.Body",
#                     "Type": "instance.Body",
#                     "Messagesid": "instance.Body",
#                     "fromNumber" : "instance.Body"
#                 #    "PhoneNumber": instance.number
#                     })