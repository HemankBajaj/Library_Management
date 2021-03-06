# Generated by Django 3.2 on 2021-04-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20210425_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuerequest',
            name='permission',
            field=models.CharField(choices=[(False, 'denied'), (True, 'issued')], default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='issuerequest',
            name='status',
            field=models.CharField(choices=[(False, 'pending'), (True, 'seen')], default='', max_length=30),
        ),
    ]
