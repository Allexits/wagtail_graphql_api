from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from modelcluster.fields import ParentalKey
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from grapple.models import GraphQLString, GraphQLImage, GraphQLForeignKey, GraphQLCollection


class AgentsPage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = []
    
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels+[
        FieldPanel('body'),
        MultiFieldPanel([InlinePanel('page_agents', label='Agent')]),
    ]

    graphql_fields = [
        GraphQLString('body'),
        GraphQLCollection(GraphQLForeignKey, 'page_agents', 'agents.AgentsConnection')
    ]


@register_snippet
class Agents(models.Model):

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        )
    name = models.CharField(max_length=255)
    desc = RichTextField(blank=True)
    phone = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    first_parent = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel('image'),
        FieldPanel('name'),
        FieldPanel('desc'),
        FieldPanel('phone'),
        FieldPanel('email'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Agent"
        verbose_name_plural = "Agents"

    graphql_fields = [
        GraphQLImage('image'),
        GraphQLString('name'),
        GraphQLString('desc'),
        GraphQLString('phone'),
        GraphQLString('email'),
        GraphQLString('first_parent'),
    ]


class AgentsConnection(Orderable):
    page = ParentalKey('agents.AgentsPage', related_name='page_agents', on_delete=models.CASCADE)
    agent = models.ForeignKey('agents.Agents',  null=True, blank=True, on_delete=models.CASCADE)
    panels = [FieldPanel('agent')]
    graphql_fields = [
        GraphQLForeignKey('agent', content_type='agents.Agents')
    ]