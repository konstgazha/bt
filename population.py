import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'businessterritory.settings')

import django
django.setup()
from core.models import Organization, Activity, OrganizationActivity,\
                        Pledge, Request, RequestPledge
import pandas as pd


def create_or_update_organization(**kwargs):
    organization = Organization.objects.get_or_create(kwargs['inn'])[0]
    organization.save()
    organization.update(**kwargs)


def create_or_update_organization_activity(organization, activity, main):
    org_activity = OrganizationActivity.objects.get_or_create(organization=organization,
                                                              activity=activity)[0]
    org_activity.main = main
    org_activity.save()


def create_or_update_pledge(name):
    pledge = Pledge.objects.get_or_create(name=name)[0]
    pledge.save()
    

def create_or_update_activity(name):
    activity = Activity.objects.get_or_create(name=name)[0]
    activity.save()


def create_or_update_request(organization, signing_date, pledge_date, credit_amount, pledge_amount):
    request = Request.objects.get_or_create(organization=organization,
                                            signing_date=signing_date)[0]
    request.pledge_date = pledge_date
    request.credit_amount = credit_amount
    request.pledge_amount = pledge_amount
    request.save()


def create_or_update_request_pledge(request, pledge, value):
    activity = RequestPledge.objects.get_or_create(request=request,
                                                   pledge=pledge)[0]
    activity.value = value
    activity.save()


def populate_from_csv(filename, sep=';', decimal=','):
    df = pd.read_csv(filename, sep=sep, decimal=decimal)