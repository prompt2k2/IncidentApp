# Generated by Django 3.2.3 on 2021-08-17 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IMRegister', '0009_auto_20210817_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incident',
            old_name='siteID',
            new_name='SiteID',
        ),
    ]