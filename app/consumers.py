import json
import logging

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


logger = logging.getLogger('application')


class AppConsumer(WebsocketConsumer):
    """A simple consumer for websocket connections between the client and host.

    Allows for establishing one of multiple potential groups for communication.
    Messages can be sent to the consumer and then echoed back to the whole group
    or Python code (eg. Django database signals) can trigger sending of the
    message host-side using the notify method.
    """
    def __init__(self):
        super(AppConsumer, self).__init__()
        self.group_name = None

    def connect(self):
        """Join a channel layer group based on the URL used to access socket."""
        # fetch group name from connection request
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        logger.info(f'Received connection request for group: {self.group_name}')
        logger.info(f'Connecting to {self.group_name}...')

        # join the group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()
        logger.info(f'Connection to {self.group_name} successful!')

    def disconnect(self, code):
        """Leave the group with the given code"""
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def message(self, event):
        """Send a message

        Combine with channel_layer.group_send to send a message to all in group.
        """
        logger.info(f"Sending message: {event['message']}...")
        self.send(text_data=json.dumps({'message': event['message']}))
        logger.info(f"Sent!")

    def receive(self, text_data: str=None, bytes_data: bytes=None):
        """Receive a message from a client within group and broadcast back."""
        if not text_data and bytes_data:
            text_data = bytes_data.decode()

        # extract message
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        logger.info(f'received message: {message}')

        # send message back
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'message',
                'message': message
            }
        )

    def notify(self, event):
        """Handle calls elsewhere in codebase to send a message to websocket

        channel_layer.group_send(group_name, {
            'type': 'notify',  # route to this handler
            'content': json_message
        })
        """
        logger.info(f"Notified of message, sending to group: {self.group_name}...")
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'message',
                'message': event['content']
            }
        )