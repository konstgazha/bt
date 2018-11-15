from django.db import models


class Organization(models.Model):
    inn = models.CharField(max_length=128, unique=True, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    rating = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=128, blank=True, null=True)
    registry = models.BooleanField(blank=True, null=True)
    registration_date = models.DateTimeField(blank=True, null=True)
    employees_number = models.IntegerField(blank=True, null=True)
    planned_employees_number = models.IntegerField(blank=True, null=True)
    plaintiff_count = models.IntegerField(blank=True, null=True)
    defendant_count = models.IntegerField(blank=True, null=True)
    plaintiff_sum = models.IntegerField(blank=True, null=True)
    defendant_sum = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    previous_year_revenue = models.IntegerField(blank=True, null=True)
    planned_revenue = models.IntegerField(blank=True, null=True)


class Activity(models.Model):
    name = models.CharField(max_length=128)


class OrganizationActivity(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    main = models.BooleanField(default=False)


class Pledge(models.Model):
    name = models.CharField(max_length=128)


class Request(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    signing_date = models.DateTimeField(blank=True, null=True)
    pledge_date = models.DateTimeField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    pledge_amount = models.FloatField(blank=True, null=True)


class RequestPledge(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    pledge = models.ForeignKey(Pledge, on_delete=models.CASCADE)
    value = models.IntegerField(blank=True, null=True)