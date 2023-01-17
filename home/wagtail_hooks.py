from wagtail import hooks
from wagtail.documents.wagtail_hooks import DocumentsMenuItem
from wagtail.snippets.wagtail_hooks import SnippetsMenuItem


HIDDEN_MENU_ITEMS = (
    SnippetsMenuItem,
    DocumentsMenuItem,
)


@hooks.register('construct_main_menu')
def hide_snippets_menu_item(request, menu_items):
    def is_shown(item) -> bool:
        for menu_item_type in HIDDEN_MENU_ITEMS:
            if isinstance(item, menu_item_type):
                return False
        return True
    menu_items[:] = list(filter(is_shown, menu_items))  