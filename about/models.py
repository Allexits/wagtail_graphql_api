from wagtail.core.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel 


class AboutPage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = []
    
    body = RichTextField(blank=True)

    content_panels = Page.content_panels+[
        FieldPanel('body')
    ]