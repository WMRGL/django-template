# django-template
A template from which django apps can be started pre-loaded with:
- *Django utilities*: Channels, Celery + Celerybeat, Django REST Framework, EasyAudit, Django-Extensions/IPython Shell.
- *Web utitilies*: JQuery, SemanticUI CSS, DataTables.

### Steps
- Click 'use this template' at the top right of this page and create your repo. 
- `pip install -r requirements.txt` in your venv
- Change the name of 'project' and 'app' to whatever you like. You can even leave them the same if you want.
- Duplicate the 'project/settings/example_local.py' file to 'project/settings/local.py' and enter necessary security and database details.
- Run migrations: `python manage.py migrate; python manage.py migrate app`.
- Set up auditing: `python manage.py migrate easyaudit`.

## Logging
- To add log calls (rather than prints which are not picked up using the gunicorn method in the django SOP) use:
```Python
import logging
logger = logging.getLogger('application')
logger.info('info log')
logger.error('error log')  # etc etc
```
- Database calls can be logged too if the environment variable DJANGO_LOG_LEVEL is set to 'DEBUG' before running runserver/gunicorn

## Django REST Framework
More info here: https://www.django-rest-framework.org/
- Add endpoints in the app.endpoints module; add URLs to the endpoints in app.routing module by registering the endpoint with the router.
- Endpoints will be at http://hostname:port/api/...

## Celery
More info here: https://docs.celeryproject.org/en/stable/index.html
- Set up a RabbitMQ virtualhost (section 10 of Django SOP) and add the credentials to `settings.local.CELERY_BROKER_URL`. 
- Run the celery_start and celerybeat_start scripts in django_template/scripts
- Add new celery tasks in app.tasks as desired and call them with eg. `task = func.delay(*args, **kwargs)` to call them asynchronously. `task.state` indicates completion status, `task.get()` has the return value.
- By default the test task is called once a minute to test celerybeat is set up correctly. Modify this in project.settings.base CELERY_BEAT_SCHEDULER

## Channels
More info here: https://channels.readthedocs.io/en/stable/
- Set up a RabbitMQ virtualhost (section 10 of Django SOP) and add the credentials to `settings.local.CHANNEL_LAYERS['default']['CONFIG']['host']` (or use the same as for Celery). 
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
- There is a simple consumer already set up for messages, it is recommended to reconfigure this or make your own for more complex behaviours.

## Additional features
- The `app.models` includes a custom User model which subclasses the original User model so that additional fields can be added if required; Django prevents any attempt to create a custom User model following the first migration otherwise. See here for how to reference this model: https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#referencing-the-user-model
- running `python manage.py shell_plus` gives you an IPython shell with models pre-imported

# TO DO
- add django-rest-framework
- add shell_plus ipython notebook support
