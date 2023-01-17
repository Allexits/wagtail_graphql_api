from simple_salesforce import Salesforce
from .settings import SALESFORCE_USERNAME, SALESFORCE_SECURITY_TOKEN, SALESFORCE_PASSWORD, SALESFORCE_INSTANCE, SALESFORCE_USE_SANDBOX


def login():
    return Salesforce(
        username= SALESFORCE_USERNAME,
        password= SALESFORCE_PASSWORD,
        security_token= SALESFORCE_SECURITY_TOKEN,
        instance_url = SALESFORCE_INSTANCE,
    )