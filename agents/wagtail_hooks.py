from wagtail.contrib.modeladmin.options import(ModelAdmin, modeladmin_register)
from .models import Agents
from blog.models import BlogDetailPage
from wagtail.core import hooks
from agents.queries import AgentsQuery 

@modeladmin_register
class AgentsAdmin(ModelAdmin):
    model=Agents
    list_display=('name',)
    menu_label='Agents:'
    menu_icon='pilcrow'


@hooks.register("register_schema_query")
def add_my_custom_query(query_mixins):
    query_mixins.append(AgentsQuery)    