# Generated by Django 3.2 on 2021-04-25 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_auto_20210425_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuerequest',
            name='issue_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issuerequest',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
