from django.db import models
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):
    name = models.CharField(_('autor'), max_length=60)

    class Meta:
        verbose_name = _('Autor')
        verbose_name_plural = _('Autores')
        ordering = ['name']

    def __str__(self):
        return self.name
