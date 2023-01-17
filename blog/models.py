from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


class BlogPage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['blog.BlogDetailPage']

    title_desc = models.CharField(max_length=255, null=True, blank=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels+[
        FieldPanel('body')
    ]


class BlogDetailPage(Page):
    parent_page_types = ['blog.BlogPage']
    subpage_types = []

    first_parent = models.CharField(max_length=255, blank=True)
    
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        )
    related = models.ForeignKey(
        'blog.BlogRelated',
        null= True,
        blank= True,
        on_delete= models.SET_NULL,
        related_name= '+'
    )    
    
    desc = RichTextField()

    content_panels = Page.content_panels+[
        FieldPanel('image'),
        FieldPanel('related',classname="full"),
        FieldPanel('desc')
    ]


@register_snippet
class BlogRelated(models.Model):

    title = models.CharField(max_length=255)

    panels = [
        FieldPanel('title')
    ]

    def __str__(self):
        return self.title