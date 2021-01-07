# django-template
a template from which django apps can be started pre-loaded with celery, channels, and logging

Steps
- Make your own repo
- Download the source code from this repo as a zip and add to your git repo
- Change the name of 'project' and 'app' to whatever you like
- migrate

## Logging
- To add log calls (rather than prints which are not picked up using the gunicorn method in the django SOP) use:
```Python
import logging
logger = logging.getLogger('application')
logger.info('info log')
logger.error('error log')  # etc etc
```
- Database calls can be logged too if the environment variable DJANGO_LOG_LEVEL is set to 'INFO' before running runserver/gunicorn

## Celery
More info here: https://docs.celeryproject.org/en/stable/index.html
- Run the celery_start and celerybeat_start scripts in django_template/scripts
- Add new celery tasks in app.tasks as desired and call them with eg. `task = func.delay(*args, **kwargs)` to call them asynchronously. `task.state` indicates completion status, `task.get()` has the return value.
- By default the test task is called once a minute to test celerybeat is set up correctly. Modify this in project.settings.base CELERY_BEAT_SCHEDULER

## Channels
More info here: https://channels.readthedocs.io/en/stable/
- Channels allow asynchronous messaging between a client and host using a websocket.
- websocket urls are set up in `app.routing`, websocket request consumers (similar to views but for websocket requests) are set up in `app.consumers`
- to establish a websocket connection on a client page:
```JavaScript
const applicationSocket = new WebSocket('ws://' + window.location.host + '<websocket_path>' )
// to process received data:
applicationSocket.onmessage = function(e) { 
// function which executes when Websocket sends message to client via its self.send() method
    const data = JSON.parse(e.data) 
    ...
} 
// to send data which is processed using the websocket's self.receieve() method:
data = {}
applicationSocket.send(JSON.stringify(data))
```

## Additional features
- running `python manage.py shell_plus` gives you an IPython shell with models pre-imported

# TO DO
- add django-rest-framework
- add shell_plus ipython notebook support
