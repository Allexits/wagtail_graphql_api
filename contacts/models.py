from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class ContactsPage(Page):
    parent_page_type = ['wagtailcore.Page']
    subpage_types = []
    
    body = RichTextField(blank=True)

    content_panels = Page.content_panels+[
        FieldPanel('body')
    ]
