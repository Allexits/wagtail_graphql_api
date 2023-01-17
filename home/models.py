from django.db import models

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from grapple.helpers import register_singular_query_field
from wagtail_headless_preview.models import HeadlessMixin
from modelcluster.fields import ParentalKey
from grapple.models import GraphQLString, GraphQLImage, GraphQLForeignKey, GraphQLCollection

class HomePage(HeadlessMixin, Page):
    #subpage_types = []
    #preview_modes =[]

    body = RichTextField(blank=True)


    content_panels = Page.content_panels+[
        FieldPanel('body'),
        InlinePanel('page_sliders')
    ]
    graphql_fields = [
        GraphQLString('body'),
        GraphQLCollection(GraphQLForeignKey, 'page_sliders', 'agents.AgentsConnection')
    ]

class SliderConnection(Orderable):
    page = ParentalKey('home.HomePage', related_name='page_sliders',on_delete=models.CASCADE) 
    slider = models.ForeignKey('slider.Slider',  null=True, blank=True, on_delete=models.CASCADE)
    graphql_fields = [
        GraphQLForeignKey( 'slider', 'slider.Slider')
    ]
    def __str__(self):
        return self.slider.get_image