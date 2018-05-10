from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Link(models.Model):
    url = models.URLField(db_index=True, unique=True)

    def __str__(self):
        return self.url

    def get_absolute_url(self):
        return self.url
