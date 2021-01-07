#!/usr/bin/env bash
source venv
celery -A yourhonr beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
