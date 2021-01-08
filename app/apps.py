from django.apps import AppConfig


class ApplicationConfig(AppConfig):
    name = 'app'

    def ready(self):
        import app.handlers
