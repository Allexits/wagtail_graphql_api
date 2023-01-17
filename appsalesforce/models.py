from salesforce import models
from salesforce.models import SalesforceModel
from wagtail.snippets.models import register_snippet


class Contact(SalesforceModel):
    Title = models.CharField(max_length=255, blank=False, null=False)
