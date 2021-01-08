import logging

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver


User = get_user_model()
logger = logging.getLogger('application')


@receiver(signals.post_save, sender=User)
def user_save_handler(sender, **kwargs):
    """Execute when a user is created or modified."""
    instance = kwargs['instance']
    created = kwargs['created']
    message = f'User {instance} was {"created" if created else "modified"}.'
    message_consumer('users', message)


@receiver(signals.post_delete, sender=User)
def user_delete_handler(sender, **kwargs):
    """Execute when a user instance is deleted"""
    instance = kwargs['instance']
    message = f'User {instance} was deleted.'
    message_consumer('users', message)


def message_consumer(group, message):
    """Take a message from a handler and send it to the relevant group."""
    logger.info(message)
    # send a notification to the user websocket consumer
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        group,
        {
            'type': 'notify',
            'content': message
        }
    )
