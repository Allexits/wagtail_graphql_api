from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Slider

@modeladmin_register
class SliderAdmin(ModelAdmin):
    model=Slider
    list_display=('title', 'get_image')
    menu_label='Slider:'
    menu_icon='pilcrow'    