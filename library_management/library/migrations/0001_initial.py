# Generated by Django 3.2 on 2021-04-23 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('isbn', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=40)),
                ('genre', models.CharField(choices=[('academics', 'Academics'), ('fiction', 'Fiction'), ('action ', 'Action '), ('biography', 'Biography'), ('history', 'History'), ('mystery', 'Mystery'), ('fantasy', 'Fantasy')], default='academics', max_length=30)),
                ('number', models.PositiveIntegerField()),
            ],
        ),
    ]