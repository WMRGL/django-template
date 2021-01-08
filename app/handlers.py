import logging

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
    logger.info(f'User {instance} was {"created" if created else "modified"}.')


@receiver(signals.post_delete, sender=User)
def user_delete_handler(sender, **kwargs):
    """Execute when a user instance is deleted"""
    instance = kwargs['instance']
    logger.info(f'User {instance} was deleted.')
