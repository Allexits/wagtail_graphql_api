from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from grapple.helpers import register_singular_query_field
from modelcluster.fields import ParentalKey
from grapple.models import GraphQLString, GraphQLImage, GraphQLForeignKey, GraphQLCollection


@register_singular_query_field('home')
class HomePage(Page):
    parent_page_types = ['wagtailcore.Page']
    subpage_types = []
    body = RichTextField(blank=True)

    content_panels = Page.content_panels+[
        FieldPanel('body'),
        MultiFieldPanel([InlinePanel('sliders', label='Slider')])
    ]

    graphql_fields = [
        GraphQLString('body'),
        GraphQLCollection(GraphQLForeignKey, 'sliders', 'home.SliderHomePage')
    ]


class SliderHomePage(Orderable):
    home = ParentalKey('home.HomePage', related_name='sliders', on_delete=models.CASCADE)
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    title = models.CharField(max_length=255, null=True)
    alt = models.CharField(max_length=255, null=True)

    panels = [
        MultiFieldPanel([
                 FieldPanel('image'),
                 FieldPanel('title'),
                 FieldPanel('alt')
            ], heading='Sliders'),
    ]

    graphql_fields = [
        GraphQLString('image'),
        GraphQLString('title'),
        GraphQLString('alt'),
    ]

    def __str__(self):
        return self.title