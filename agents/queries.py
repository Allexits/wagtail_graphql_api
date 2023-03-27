import graphene
from graphene_django import DjangoObjectType, DjangoListField
from agents.models import AgentsPage, Agents
from django.db.models import Q

class AgentsPageType(DjangoObjectType):
    class Meta:
        model = AgentsPage
        fields = (
            'id',
            'title',
            'page_agents',
            )

class AgentsType(DjangoObjectType):
    class Meta:
        model = Agents
        fields = (
            'id',
            'name',

            )


class AgentsQuery(graphene.ObjectType):
    agent = graphene.Field(AgentsType, id = graphene.Int())
    agents = graphene.List(AgentsType)
    agentspage = graphene.List(AgentsPageType, search = graphene.String())

    def resolve_agent(self, info, id):
        return Agents.objects.get(pk=id)

    def resolve_agents(self, info):
        return Agents.objects.all()

    def resolve_agentspage(self, info, **kwargs):
        search = kwargs.get('search')
        data = AgentsPage.objects.all()
        return data