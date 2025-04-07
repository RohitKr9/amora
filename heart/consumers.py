from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import DenyConnection
from asgiref.sync import async_to_sync
import json

class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        user = self.scope['user'] #it contains user object

        if user.is_anonymous:
            raise DenyConnection() #This is not mentioned in documentation (Way to close connection )
        
        user_id = user.id
        self.room_name = f"room_{user_id}"
        self.room_group_name = self.room_name
        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name) #all channel layer methods are async
        self.accept()

    def disconnect(self, closing_code):
        print(f'There is something wrong -> Code = {closing_code}')

    def receive(self, text_data):
        text_data_loaded = json.loads(text_data)
        message = text_data_loaded['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type":"chat_message",
                "message" : message
            }
        )
    
    def chat_message(self, event):
        message = event["message"]
        self.send(text_data = json.dumps({"message":message}))