from django.conf import settings


def version(request):
    """Return the current version of the application inside any template."""
    return {'version': settings.VERSION}
