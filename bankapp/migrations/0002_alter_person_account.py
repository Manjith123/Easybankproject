# Generated by Django 3.2.13 on 2022-08-24 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='account',
            field=models.CharField(choices=[('Current Account', 'Current Account'), ('Saving Account', 'Saving Account')], max_length=100),
        ),
    ]
