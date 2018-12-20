from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Message
from accounts.models import User

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'chatter'
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        user_id = int(text_data_json['user_id'])
        username = text_data_json['username']
        message = text_data_json['message']

        #save the message to the database
        user = User.objects.get(pk=user_id)
        messageObj = Message.create_message(content=message, user=user)
        messageObj.save()

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username': username,
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        user = event['username']
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'username': user,
            'message': message
        }))