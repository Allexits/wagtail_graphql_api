from django.db import models
from django.utils.html import mark_safe
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet
from grapple.models import GraphQLImage, GraphQLString


@register_snippet
class Slider(models.Model):
    title = models.CharField(max_length=255, null=True)
    alt = models.CharField(max_length=255, null=True)
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        FieldPanel('image'),
        FieldPanel('title'),
        FieldPanel('alt'),
    ]

    graphql_fields = [
        GraphQLString('title'),
        GraphQLString('alt'),
        GraphQLImage('image'),
    ]

    def __str__(self):
        return self.title
    