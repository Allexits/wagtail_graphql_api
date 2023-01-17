from wagtail.contrib.modeladmin.options import(ModelAdmin, modeladmin_register)
from .models import BlogDetailPage
from wagtail.core import hooks


@hooks.register('after_create_page')
def set_attribute_after_page_create(request, page=BlogDetailPage):
    first_parent = page.get_parent().specific._meta.model_name
    page.first_parent = first_parent
    new_revision = page.save_revision()
    if page.live:
        new_revision.publish()
