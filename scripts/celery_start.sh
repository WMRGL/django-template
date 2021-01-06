#!/usr/bin/env bash
source /home/theo/channels/bin/activate
celery -A yourhonr worker -l info
