from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtailorderable.modeladmin.mixins import OrderableMixin
from menu.models import MenuPage

@modeladmin_register
class MenuAdmin(OrderableMixin, ModelAdmin):
    model = MenuPage
    list_display = ('title',)
    menu_label = 'Menu:'
    menu_icon = 'pilcrow'