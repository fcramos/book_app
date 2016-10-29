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


class Category(models.Model):
    description = models.CharField(_('descrição'), max_length=20)

    class Meta:
        verbose_name = _('Categoria')
        verbose_name_plural = _('Categorias')
        ordering = ['description']

    def __str__(self):
        return self.description


class Book(models.Model):
    title = models.CharField(_('título'), max_length=60)
    author = models.ForeignKey(Author)
    category = models.ForeignKey(Category)
    pages = models.PositiveIntegerField(_('número de páginas'))
    description = models.TextField(_('descrição'), blank=True, null=True)
    published_in = models.DateField(_('publicado em'))

    class Meta:
        verbose_name = _('Livro')
        verbose_name_plural = _('Livros')
        ordering = ['title']

    def __str__(self):
        return self.title
