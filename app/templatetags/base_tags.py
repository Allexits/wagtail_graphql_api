from django import template
from wagtail.core.models import Site

register = template.Library()

#navigation_menu
@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context['request']).root_page


@register.inclusion_tag('tags/nav_menu.html', takes_context=True)
def nav_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.active = (calling_page.url_path.startswith(menuitem.url_path) if calling_page else False)

    return {      
        'calling_page':calling_page,  
        'menuitems': menuitems,
        'request': context['request'],
    }

#footer
@register.inclusion_tag('tags/footer_menu.html', takes_context=True)
def footer_menu(context):
    menuitems = Site.find_for_request(context['request']).root_page.get_children().live().in_menu()

    return {       
        'menuitems': menuitems,
        'request': context['request'],
    }
