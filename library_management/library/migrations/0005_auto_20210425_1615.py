# Generated by Django 3.2 on 2021-04-25 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20210425_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuerequest',
            name='permission',
            field=models.CharField(choices=[('', ''), ('issued', 'issued')], default='', max_length=30),
        ),
        migrations.AddField(
            model_name='issuerequest',
            name='status',
            field=models.CharField(choices=[('', ''), ('seen', 'seen')], default='', max_length=30),
        ),
    ]