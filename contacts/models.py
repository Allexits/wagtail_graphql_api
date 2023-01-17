from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class ContactsPage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = []
    
    body = RichTextField(blank=True)

    content_panels = Page.content_panels+[
        FieldPanel('body')
    ]
