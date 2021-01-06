import json
import logging

from channels.generic.websocket import WebsocketConsumer


logger = logging.getLogger('application')


class WorklogConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data: str=None, bytes_data: bytes=None):
        """Receive a message from a client and echo message back."""
        if not text_data and bytes_data:
            text_data = bytes_data.decode()

        # extract message
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        logger.info(f'received message: {message}')

        # send message
        self.send(text_data=json.dumps({'message': message}))
