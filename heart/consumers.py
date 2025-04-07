from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import DenyConnection

class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        user = self.scope['user'] #it contains user object
        user_id = user.id

        if user.is_anonymous:
            raise DenyConnection() #This is not mentioned in documentation (Way to close connection )
        
        self.accept()

    def disconnect(self, closing_code):
        
        print(f'There is something wrong -> Code = {closing_code}')

    def receive(self, text_data):
        pass