from django.conf import settings
from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^(?P<prefix>{0!s})(?P<tiny>\w+)$'.format(
            '|'.join(settings.SHORTEN_MODELS.keys())),
        views.redirect,
    ),
]
