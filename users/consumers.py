from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
import json
from random import randint
from time import sleep
from asgiref.sync import async_to_sync

# class MessageConsumer(AsyncJsonWebsocketConsumer):

#     async def connect(self):
#         await self.accept()
#         await self.channel_layer.group_add("message", self.channel_name)
#         print(f"Added {self.channel_name} channel to message")

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard("message", self.channel_name)
#         print(f"Removed {self.channel_name} channel to message")


#     async def new_message(self, event):
#         await self.send_json(event)
#         print(f"channels working")
#         print(f"channels working")
#         print(f"channels working")
#         print(f"channels working")
#         print(f"Got message {event} at {self.channel_name}")


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'messages'
        self.room_group_name = "messages_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        # await self.channel_layer.group_add("message", self.channel_name)
        print("#######CONNECTED############")
        # for i in range(10):
        #     # print(randint(1,100))
        #     self.send(json.dumps({'message': randint(1,100)}))
        #     sleep(1)
        self.send(json.dumps({'message': 'connected with django'}))
    # def receive(self,text_data):
    #     print(text_data)

    # def scraps(self,*args,**kwargs):
    #     print('disconnect')
        
    def next_notifi(self,event):
        print('so this is eventttttttttttttttttttttttttttttttt')
        print(event)
        print(event.get('value'))
        print(event.get('body'))
        print(event.get('title'))
        print(event.get('description'))
        print(event.get('wordcount'))
        print(event.get('response_time'))
        print('so this is eventmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
        self.send(json.dumps(
            {
                'et': event.get('value'),
                'body': event.get('body'),
                'title': event.get('title'),
                'description': event.get('description'),
                'wordcount': event.get('wordcount'),
                'response_time': event.get('response_time'),
            }))

class NewConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.room_name = 'notifications'
        self.room_group_name = "notifications_group"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # await self.channel_layer.group_add("message", self.channel_name)
        await self.accept()
        print("*************************************************CONNECTED############")
        # for i in range(10):
        #     # print(randint(1,100))
        #     self.send(json.dumps({'message': randint(1,100)}))
        #     sleep(1)
        await self.send(json.dumps({'message': ' new connection has been eastablished with django'}))
    
    async def receive(self, text_data):
        print(text_data)
        await self.send(json.dumps(
            {
                'et': 'HAsni',
            }))    

    
    async def next_notifi(self,event):
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        # await print(event)
        print(event.get('value'))
        # print(event.get('body'))
        print(event.get('title'))
        print(event.get('description'))
        print(event.get('wordcount'))
        print(event.get('response_time'))
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        await self.send(json.dumps(
            {
                'et': event.get('value'),
                # 'body': event.get('body'),
                'title': event.get('title'),
                'description': event.get('description'),
                'wordcount': event.get('wordcount'),
                'response_time': event.get('response_time'),
            }))
            
    async def disconnect(self,*args,**kwargs):
        print('disconnected')