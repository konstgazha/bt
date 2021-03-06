# Generated by Django 2.1.2 on 2018-11-15 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.IntegerField(blank=True, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('rating', models.CharField(blank=True, max_length=128, null=True)),
                ('status', models.CharField(blank=True, max_length=128, null=True)),
                ('registry', models.BooleanField(blank=True, null=True)),
                ('registration_date', models.DateTimeField(blank=True, null=True)),
                ('employees_number', models.IntegerField(blank=True, null=True)),
                ('planned_employees_number', models.IntegerField(blank=True, null=True)),
                ('plaintiff_count', models.IntegerField(blank=True, null=True)),
                ('defendant_count', models.IntegerField(blank=True, null=True)),
                ('plaintiff_sum', models.IntegerField(blank=True, null=True)),
                ('defendant_sum', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('previous_year_revenue', models.IntegerField(blank=True, null=True)),
                ('planned_revenue', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.BooleanField(default=False)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Activity')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Pledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signing_date', models.DateTimeField(blank=True, null=True)),
                ('pledge_date', models.DateTimeField(blank=True, null=True)),
                ('credit_amount', models.FloatField(blank=True, null=True)),
                ('pledge_amount', models.FloatField(blank=True, null=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='RequestPledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True)),
                ('pledge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pledge')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Request')),
            ],
        ),
    ]
