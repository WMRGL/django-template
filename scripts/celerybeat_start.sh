#!/usr/bin/env bash
source /home/theo/channels/bin/activate
celery -A yourhonr beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
