import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'businessterritory.settings')

import django
django.setup()
from core.models import Organization, Activity, OrganizationActivity,\
                        Pledge, Request, RequestPledge, Rating, Status
import pandas as pd
import pickle
from dateutil.parser import parse


def create_or_update_organization(**kwargs):
    instance, created = Organization.objects.get_or_create(inn=kwargs['inn'])
    if not created:
        for attr, value in kwargs.items(): 
            if attr == 'registration_date':
                setattr(instance, attr, parse(value))
            else:
                setattr(instance, attr, value)
        instance.save()


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


def get_or_create_rating(name):
    rating = Rating.objects.get_or_create(name=name)[0]
    rating.save()
    return rating


def get_or_update_status(new_name):
    if 'стад' in new_name.lower() and 'реорг' in new_name.lower():
        status = Status.objects.get_or_create(name='в стадии реорганизации')[0]
    elif 'действ' in new_name.lower():
        status = Status.objects.get_or_create(name='действующий')[0]
    elif 'стад' in new_name.lower() and 'ликвид' in new_name.lower():
        status = Status.objects.get_or_create(name='в стадии ликвидации')[0]
    elif 'ликвид' in new_name.lower() or 'прекращ' in new_name.lower():
        status = Status.objects.get_or_create(name='ликвидировано')[0]
    status.save()
    return status


def load_pickle(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data


def populate_historical_data(filename):
    data = pd.read_csv(filename, encoding='ansi', decimal=',')
    for idx, row in data.iterrows():
        values = {}
        for attr, value in row.items():
            if attr == 'inn':
                if not pd.isnull(value):
                    values.update({'inn': value})
            if attr == 'rating':
                if not pd.isnull(value):
                    rating = get_or_create_rating(value)
                    values.update({'rating': rating})
            if attr == 'status':
                if not pd.isnull(value):
                    status = get_or_update_status(value)
                    values.update({'status': status})
            if attr == 'Полное наименование заёмщика':
                if not pd.isnull(value):
                    values.update({'name': value})
            if attr == 'registration_date':
                if not pd.isnull(value):
                    values.update({'registration_date': parse(value)})
            if attr == 'Численность работников по состоянию на 01 января текущего года':
                if not pd.isnull(value):
                    values.update({'employees_number': int(float(value))})
            if attr == 'Планируемое количество рабочих мест':
                if not pd.isnull(value):
                    values.update({'planned_employees_number': int(float(value))})
            if attr == 'plaintiff_count':
                if not pd.isnull(value):
                    values.update({'plaintiff_count': int(value)})
            if attr == 'defendant_count':
                if not pd.isnull(value):
                    values.update({'defendant_count': int(value)})
            if attr == 'plaintiff_sum':
                if not pd.isnull(value):
                    values.update({'plaintiff_sum': float(value)})
            if attr == 'defendant_sum':
                if not pd.isnull(value):
                    values.update({'defendant_sum': float(value)})
        if 'inn' in values.keys():
            create_or_update_organization(**values)


if __name__ == '__main__':
    populate_historical_data('data\history.csv')