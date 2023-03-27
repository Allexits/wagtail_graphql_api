from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, InlinePanel, PageChooserPanel
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtailorderable.models import Orderable as ModelOrderable
from grapple.models import GraphQLString, GraphQLForeignKey, GraphQLCollection,GraphQLField
from grapple.helpers import register_query_field


@register_query_field('menu')
class MenuPage(ClusterableModel, ModelOrderable):
    title = models.CharField(max_length=255)
    page = models.ForeignKey("wagtailcore.Page", on_delete=models.CASCADE)

    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            PageChooserPanel('page'),
        ], heading='Menu'),
        MultiFieldPanel([
            InlinePanel('children', label='Children')
        ], heading='Children')
    ]

    @property
    def link(self):
        if self.page:
            return self.page.url_path
        return '#'

    graphql_fields = [
        GraphQLString('title'),
        GraphQLString('link'),
        GraphQLCollection(GraphQLForeignKey, 'children', 'menu.ChildrenMenuPage')
    ]

    def __str__(self):
        return self.title


class ChildrenMenuPage(Orderable):
    menu = ParentalKey('menu.MenuPage', related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    page = models.ForeignKey("wagtailcore.Page", on_delete=models.CASCADE)

    panels = [
            FieldPanel('title'),
            PageChooserPanel('page'),

    ]

    @property
    def link(self):
        if self.page:
            return self.menu.link+self.page.url_path[1:]
        return '#'

    graphql_fields = [
        GraphQLString('title'),
        GraphQLString('link')
    ]