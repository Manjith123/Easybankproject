# Generated by Django 3.2.13 on 2022-08-24 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_alter_person_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100),
        ),
    ]
