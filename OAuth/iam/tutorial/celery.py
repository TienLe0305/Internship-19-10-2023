import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iam.settings')
app = Celery('tutorial', broker="pyamqp://guest@localhost//")

# Configure Celery logging
# app.log.setup(loglevel="INFO", colorize=True, task_formatter="tutorial.tasks.clear_tokens")

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

CELERYD_LOG_LEVEL = 'DEBUG'
CELERYD_LOG_FILE = 'worker.log'