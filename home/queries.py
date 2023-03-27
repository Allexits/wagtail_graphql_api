import graphene
from graphene_django import DjangoObjectType, DjangoListField
from home.models import HomePage
from wagtail.core.models import Page
from django.db.models import Q


class MenuhType(DjangoObjectType):
    class Meta:
        model = Page
        fields = ('slug', 'title',)


class HomeQuery(graphene.ObjectType):
    menuh = graphene.List(MenuhType)

    def resolve_menuh(self, info):
        return Page.objects.live().in_menu()
