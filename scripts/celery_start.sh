#!/usr/bin/env bash
source venv
celery -A project worker -l info
